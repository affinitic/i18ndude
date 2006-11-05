"""Tests for the message string extraction tool.
"""

import unittest
from zope.testing.doctestunit import DocTestSuite

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('i18ndude.extract'),
        ))

if __name__ == '__main__':
    unittest.main()
