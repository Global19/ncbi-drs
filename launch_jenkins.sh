#!/bin/bash

# REMINDER: Must call get_saml_credential.sh and export AWS keys
# Monitor via https://fs.ncbi.nlm.nih.gov/adfs/ls/idpinitiatedsignon

if [ -z "$AWS_ACCESS_KEY_ID" ]; then
    echo "Call get_saml_credential.sh and export"
    exit
fi

readonly INSTANCE="t3a.micro" # nano doesn't have enough RAM
readonly KEY_NAME=$USER
readonly SUBNET=subnet-4f505738
readonly SGID=sg-5d37473a
# sg-a53e35ce allows 0.0.0.0:8080
# sg-5d37473a allows RDP (3389)
readonly EXPIRES="480" # in minutes

AMI=$(aws ssm get-parameters \
    --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 \
    --region us-east-1 | jq -r '.Parameters[0].Value')



# aws --region us-east-1 ec2 describe-images --owners aws-marketplace \
    #    --filters Name=product-code,Values=aw0evgkw8e5c1q413zgy5pjce | grep 180
#AMI="ami-d5bf2caa"
distro="Amazon Linux 2 LTS" # 2 LTS
titledistro="$distro"
login="ec2-user"

declare -A tags
tags["Project"]="VDB"
name="VDB DRS $titledistro Build"
tags["Name"]="$name"
tags["Owner"]=$USER
tags["Created"]=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
tags["Expires"]=$(date -d "+$EXPIRES minutes" -u +"%Y-%m-%dT%H:%M:%SZ")
tags["Creator"]=$(basename "$0")
tags["Description"]="VDB DRS $titledistro builder. Started from $HOSTNAME."

tagstr=""
for key in "${!tags[@]}"; do
    tagstr="{\"Key\":\"${key}\",\"Value\":\"${tags[${key}]}\" },$tagstr"
done
tagstr=${tagstr: : -1} # remove trailing comma

script=$(mktemp --tmpdir aws_scriptXXX)
json=$(mktemp --tmpdir aws_jsonXXX)
#reqout=$(mktemp --tmpdir aws_reqXXX)
#filter=$(mktemp --tmpdir aws_filterXXX)

trap '/bin/rm -f $script $json' INT HUP ALRM EXIT QUIT

cat >> "$script" << ENDSCRIPT
#!/bin/bash
# Output from this script can be found in /var/log/cloud-init-output.log

nohup shutdown -P +$EXPIRES > /home/ec2-user/shutdown_out 2>&1  &

sleep 50 # Wait for cloud-init updater to finish

# Place Jenkins workdir on NVMe SSD
#if [[ -b /dev/nvme1n1 ]]; then
#    echo "Moving Jenkins to NVMe SSD"
#    mkfs -t xfs -f /dev/nvme1n1
#    mkdir /var/lib/jenkins
#    mount /dev/nvme1n1 /var/lib/jenkins
#    chgrp jenkins /var/lib/jenkins
#    chmod ug+rwx /var/lib/jenkins
#fi


yum -y install java
# Install LTS version of Jenkins
wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum -y install jenkins

yum -u install docker python3 httpd mod_wsgi

yum -y --exclude=kernel.* update &

pip3 install connexion python_dateutil setuptools \
             flask_testing coverage \
             nose pluggy py randomize black pylint &

update-motd

iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080


service docker start
service jenkins start
chkconfig jenkins on

#sudo groupadd docker
#systemctl start jenkins.service
#systemctl enable jenkins.service # Not that we expect a reboot

usermod -aG docker ec2-user
usermod -aG docker jenkins


#cat /var/lib/jenkins//secrets/initialAdminPassword

ENDSCRIPT
readonly b64json=$(base64 -w 0 "$script")

    #"UserData": "$b64json",
cat > "$json" << ENDJSON
{
    "ImageId": "$AMI",
    "InstanceType": "$INSTANCE",
    "KeyName": "$KEY_NAME",
    "MaxCount": 1,
    "MinCount": 1,
    "Monitoring": { "Enabled": true },
    "SecurityGroupIds": [ "$SGID" ],
    "SubnetId": "$SUBNET",
    "InstanceInitiatedShutdownBehavior": "terminate",
    "TagSpecifications": [
    {
        "ResourceType": "instance",
        "Tags": [
        $tagstr
        ]
    }
    ]
}
ENDJSON


cmd="aws ec2 run-instances \
    --query Instances[0].InstanceId \
    --cli-input-json file://$json \
    --user-data file://$script"
#echo "cmd is $cmd"
instance_id=$($cmd)

instance_id="${instance_id//\"}"

if [ -z "$instance_id" ]
then
    echo "Couldn't start EC2 instance" >&2
    echo -e "Command was:\n\t$cmd\n" >&2
    cat "$json"
    exit 2
fi

echo "$titledistro EC2 instance ID is $instance_id"

# TODO: Add timeout
state=""
while [[ ! $state =~ running ]]
do
    state=$(aws ec2 describe-instances --instance-ids "$instance_id"  | jq -r '.Reservations[0].Instances[0].State.Name')
    echo "  State of $instance_id is: $state"
    sleep 5
done


ret=1
while [[ $ret -ne 0 ]]
do
    sleep 20

    ip_addr=$(aws ec2 describe-instances --instance-ids "$instance_id" | jq -r '.Reservations[0].Instances[0].PublicIpAddress')
    echo "  EC2 IP Address is $ip_addr"
    echo "  Waiting for instance to start sshd ..."
    nc -w 2 "$ip_addr" 22 < /dev/null > /dev/null 2>&1
    ret=$?
done


echo "ssh -2akx $login@$ip_addr"
sleep 120
echo "Jenkins should be running on http://$ip_addr"
jenkins_password=$(ssh -2akx "$login@$ip_addr" sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo "Initial Jenkins password is $jenkins_password"

#sudo docker build -t centos7 -f Dockerfile.centos7  .
#sudo docker build -t debian9 -f Dockerfile.debian9 .

# cp build/Dockerfile.*
# Copy dependencies to EC2:
# scp Dockerfile build.sh ~/devel/asm-trace/build/TeamCity.sh ubuntu@54.166.139.160:
# sudo docker build -t ubuntu . # Creates image
# sudo docker images # Lists images
# sudo docker save -o out.tar image # image to tar
# sudo docker run -it image-id # Creates container from image and runs
# Could also docker create and then docker start
# sudo docker run -it image-id bash # debugging
# sudo docker ps # Shows "running" containers
# docker commit goes from container back to image


# Cleanup
# sudo docker rm -f $(sudo docker ps -a -q)
# sudo docker rmi $(sudo docker images -q)


