#!/usr/bin/env python

import sys
sys.path.insert(0, './lib')

import nose_continuous

if __name__ == "__main__":
    runner = nose_continuous.NoseContinuous(sys.argv[1:])
    runner.run()
