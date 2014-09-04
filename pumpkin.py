#!/usr/bin/python
"""exercise 2.1 and 2.2"""


import bisect
import random
import thinkstats
import math
import survey
import first
import sys
import gzip
import os
from first import Mean



if __name__ == "__main__":
    t=[1,1,1,3,3,591]
    mean,var=thinkstats.MeanVar(t)
    print "2.1---"
    print "Mean is: "
    print mean
    print "Variance is: "
    print var
    stdeV=math.sqrt(var)
    print "standard deviation is: "
    print stdeV
    print "2.2---"
    first.Summarize(data_dir='.')
    print "Answer: there is a fairly large standard deviation in the difference in hours for others (non first babies) to first babies.  Therefore, it suggest that the significance is probably low for the difference in gestation between the groups"

    
    
