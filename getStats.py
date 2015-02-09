import math
from varyGraph import getCompSizes

def median(l):
  s = sorted(l)
  if len(s)%2==0:
    return (s[len(l)/2 -1]+s[len(s)/2])/2.0
	
  return s[len(s)/2]

def mean(l):
  return sum(l)/float(len(l))

def deviation(l):
  m = mean(l)
  t = sum(map(lambda x: (x-m)**2,l))
  return math.sqrt(t/float(len(l)))


