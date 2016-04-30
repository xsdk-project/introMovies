#!/usr/bin/env python
#!/bin/env python
#
#

import os
import os.path, time,sys
import re
import time


def main(file):
  fd  = open(file)
  pv = fd.readline()
  while pv:
    if pv[0] == '$':
      for i in pv:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.2)
    else:
      print pv,
      if pv.find("=====") == -1: time.sleep(.05)
      if pv.find("Compiling") > -1: time.sleep(3)
      if pv.find("Running make on") > -1: time.sleep(2)        
      if pv.find("Compiling and installing TRILINOS") > -1: time.sleep(10)
    pv = fd.readline()
  fd.close()
#
#
if __name__ ==  '__main__':
  main(sys.argv[1])



