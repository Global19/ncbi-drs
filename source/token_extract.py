""" Extract SDL token from ga4gh wrapper """

# =============================================================================
#
#                            PUBLIC DOMAIN NOTICE
#               National Center for Biotechnology Information
#
#  This software/database is a "United States Government Work" under the
#  terms of the United States Copyright Act.  It was written as part of
#  the author's official duties as a United States Government employee and
#  thus cannot be copyrighted.  This software/database is freely available
#  to the public for use. The National Library of Medicine and the U.S.
#  Government have not placed any restriction on its use or reproduction.
#
#  Although all reasonable efforts have been taken to ensure the accuracy
#  and reliability of the software and data, the NLM and the U.S.
#  Government do not and cannot warrant the performance or results that
#  may be obtained by using this software or data. The NLM and the U.S.
#  Government disclaim all warranties, express or implied, including
#  warranties of performance, merchantability or fitness for any particular
#  purpose.
#
#  Please cite the author in any work or product based on this material.
#
# =============================================================================

import re

class TokenExtractor:
    def extract(self, wrapper: str) -> str:
        if wrapper:
            m = re.match(r'^Bearer\s+(.+)', wrapper)
            if m: return m[1]
        return None


# --------------------- Unit tests

def test_Good():
    extractor = TokenExtractor()
    token = extractor.extract('Bearer deadbeef')
    assert token == 'deadbeef'

def test_Bad1():
    extractor = TokenExtractor()
    token = extractor.extract(None)
    assert not token

def test_Bad2():
    extractor = TokenExtractor()
    token = extractor.extract('')
    assert not token

def test_Bad3():
    extractor = TokenExtractor()
    token = extractor.extract('deadbeef')
    assert not token
