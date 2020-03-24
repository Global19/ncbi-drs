# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ncbi/ncbi_log.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="ncbi/ncbi_log.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x13ncbi/ncbi_log.proto"+\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\r"\x88\x03\n\x0bstrides_log\x12\x19\n\x05start\x18\x01 \x01(\x0b\x32\n.Timestamp\x12\x17\n\x03\x65nd\x18\x02 \x01(\x0b\x32\n.Timestamp\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\r\x12\x0e\n\x06\x64omain\x18\x05 \x01(\t\x12#\n\x04\x63mds\x18\x06 \x03(\x0e\x32\x15.strides_log.HTTP_Cmd\x12\x11\n\tbytecount\x18\x07 \x01(\x04\x12\r\n\x05\x61gent\x18\x08 \x01(\t\x12\x0b\n\x03\x63nt\x18\t \x01(\x04\x12\x0b\n\x03\x61\x63\x63\x18\n \x01(\t\x12\x0e\n\x06source\x18\x0b \x01(\t\x12\x0b\n\x03msg\x18\x0c \x01(\t\x12\x0c\n\x04phid\x18\x10 \x01(\t\x12\x0e\n\x06sessid\x18\x11 \x01(\t\x12\x0f\n\x07version\x18\x12 \x01(\t"l\n\x08HTTP_Cmd\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04HEAD\x10\x01\x12\x08\n\x04POST\x10\x02\x12\x07\n\x03PUT\x10\x03\x12\n\n\x06\x44\x45LETE\x10\x04\x12\x0b\n\x07\x43ONNECT\x10\x05\x12\x0b\n\x07OPTIONS\x10\x06\x12\t\n\x05TRACE\x10\x07\x12\t\n\x05PATCH\x10\x08\x62\x06proto3'
    ),
)


_STRIDES_LOG_HTTP_CMD = _descriptor.EnumDescriptor(
    name="HTTP_Cmd",
    full_name="strides_log.HTTP_Cmd",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="GET", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HEAD", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="POST", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PUT", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DELETE", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CONNECT", index=5, number=5, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="OPTIONS", index=6, number=6, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TRACE", index=7, number=7, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PATCH", index=8, number=8, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=353,
    serialized_end=461,
)
_sym_db.RegisterEnumDescriptor(_STRIDES_LOG_HTTP_CMD)


_TIMESTAMP = _descriptor.Descriptor(
    name="Timestamp",
    full_name="Timestamp",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="seconds",
            full_name="Timestamp.seconds",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="nanos",
            full_name="Timestamp.nanos",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=23,
    serialized_end=66,
)


_STRIDES_LOG = _descriptor.Descriptor(
    name="strides_log",
    full_name="strides_log",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="start",
            full_name="strides_log.start",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="end",
            full_name="strides_log.end",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ip",
            full_name="strides_log.ip",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="strides_log.status",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="domain",
            full_name="strides_log.domain",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cmds",
            full_name="strides_log.cmds",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bytecount",
            full_name="strides_log.bytecount",
            index=6,
            number=7,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="agent",
            full_name="strides_log.agent",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="cnt",
            full_name="strides_log.cnt",
            index=8,
            number=9,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="acc",
            full_name="strides_log.acc",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="source",
            full_name="strides_log.source",
            index=10,
            number=11,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="strides_log.msg",
            index=11,
            number=12,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="phid",
            full_name="strides_log.phid",
            index=12,
            number=16,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sessid",
            full_name="strides_log.sessid",
            index=13,
            number=17,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="strides_log.version",
            index=14,
            number=18,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_STRIDES_LOG_HTTP_CMD],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=69,
    serialized_end=461,
)

_STRIDES_LOG.fields_by_name["start"].message_type = _TIMESTAMP
_STRIDES_LOG.fields_by_name["end"].message_type = _TIMESTAMP
_STRIDES_LOG.fields_by_name["cmds"].enum_type = _STRIDES_LOG_HTTP_CMD
_STRIDES_LOG_HTTP_CMD.containing_type = _STRIDES_LOG
DESCRIPTOR.message_types_by_name["Timestamp"] = _TIMESTAMP
DESCRIPTOR.message_types_by_name["strides_log"] = _STRIDES_LOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Timestamp = _reflection.GeneratedProtocolMessageType(
    "Timestamp",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMESTAMP,
        "__module__": "ncbi.ncbi_log_pb2"
        # @@protoc_insertion_point(class_scope:Timestamp)
    },
)
_sym_db.RegisterMessage(Timestamp)

strides_log = _reflection.GeneratedProtocolMessageType(
    "strides_log",
    (_message.Message,),
    {
        "DESCRIPTOR": _STRIDES_LOG,
        "__module__": "ncbi.ncbi_log_pb2"
        # @@protoc_insertion_point(class_scope:strides_log)
    },
)
_sym_db.RegisterMessage(strides_log)


# @@protoc_insertion_point(module_scope)
