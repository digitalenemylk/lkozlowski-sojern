#!/usr/bin/env python
import sys
from distutils.version import LooseVersion

# Check if the usage is correct

def check_cmdline (argv):
    if len (argv) != 3:
        print ("Usage: " + argv[0] + " <Ver1> <Ver2>")
        exit (-3);
        

def compare_ver (argv):
    if (LooseVersion(argv[1]) > LooseVersion(argv[2])):
        exit (1)
    elif (LooseVersion(argv[1]) < LooseVersion(argv[2])):
        exit (-1)
    exit (0)
 

if __name__ == "__main__":
    check_cmdline (sys.argv)
    compare_ver (sys.argv)