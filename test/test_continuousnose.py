#-*- coding: utf-8 -*-

import unittest
import nose
from nose.tools import *
import continuousnose

class TestNoseContinuous(unittest.TestCase):

    def test_init(self):
        nc = continuousnose.ContinuousNose(['--something',])
        eq_(nc.target_patterns  , ['*.py'])
        eq_(nc.target_dirs      , [])
        eq_(nc.argv             , ['--something'])

        nc = continuousnose.ContinuousNose(['--something',], patterns=['*.scala'])
        eq_(nc.target_patterns  , ['*.scala'])
        eq_(nc.target_dirs      , [])
        eq_(nc.argv             , ['--something'])

        nc = continuousnose.ContinuousNose(['--something',], dirs=['src/main'])
        eq_(nc.target_patterns  , ['*.py'])
        eq_(nc.target_dirs      , ['src/main'])
        eq_(nc.argv             , ['--something'])

