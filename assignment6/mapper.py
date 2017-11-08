#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split("/")
    if len(data)> 1:
        tempdate = data[2]
        tempdate2 = tempdate.strip().split(":")
        year = tempdate2[0]
        print str(year)
