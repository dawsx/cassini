import numpy
from math import *
import os
from pprint import pprint

target = '605'
ttime = '2011-Apr-25 19:33'
dirname = 'out-2011-04-25 1923--2011-04-25 1943 (1m)'
os.chdir(dirname)
files = os.listdir()

pos = []
for file in files:
    print (file[4:-4])
    with open(file) as f:
        for line in f:
            #print(line)
            if line.startswith(ttime):
                pos.append([file[4:-4]]+line.split(','))
                
#print(pos)
for b in pos:
    if b[0] == target:
        attrs = b

#pprint(sorted(pos, key = lambda k: abs(acos(cos(radians(float(k[2])-float(attrs[2])))*cos(radians(float(k[3])-float(attrs[3])))))))
pprint(sorted(pos, key = lambda k: (float(k[2])-float(attrs[2]))**2+(float(k[3])-float(attrs[3]))**2))
