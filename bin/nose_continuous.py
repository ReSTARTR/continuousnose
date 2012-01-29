#!/usr/bin/env python
import sys
sys.path.insert(0, './src')
import continuousnose

if __name__ == "__main__":
    runner = continuousnose.ContinuousNose(sys.argv[1:],dirs=['test','src'])
    runner.run()
