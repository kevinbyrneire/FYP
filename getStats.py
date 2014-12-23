import math, sys
from varyGraph import getCompSizes

def median(l):
  return sorted(l)[len(l)/2]

def mean(l):
  return sum(l)/float(len(l))

def deviation(l):
  m = mean(l)
  t = reduce(lambda x,y : x+y, map(lambda x: (x-m)**2,l))
  return math.sqrt(t/len(l))

filename = sys.argv[1]
stringSize = 2048
s = getCompSizes(filename, stringSize)

print median(s), mean(s), deviation(s)
