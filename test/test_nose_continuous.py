#-*- coding: utf-8 -*-

import unittest
import sys
sys.path.insert(0, './lib')
import nose_continuous
import nose
from nose.tools import *

class TestNoseContinuous(unittest.TestCase):

    def test_init(self):
        nc = nose_continuous.NoseContinuous(['--something',])
        eq_(nc.target_patterns  , ['*.py'])
        eq_(nc.target_dirs      , ['test', 'lib'])
        eq_(nc.argv             , ['--something'])

        nc = nose_continuous.NoseContinuous(['--something',], patterns=['*.scala'])
        eq_(nc.target_patterns  , ['*.scala'])
        eq_(nc.target_dirs      , ['test', 'lib'])
        eq_(nc.argv             , ['--something'])

        nc = nose_continuous.NoseContinuous(['--something',], dirs=['src/main'])
        eq_(nc.target_patterns  , ['*.py'])
        eq_(nc.target_dirs      , ['src/main'])
        eq_(nc.argv             , ['--something'])

