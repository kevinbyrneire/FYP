from varyGraphCopy import getCompSizes
import matplotlib.pyplot as plt
import sys

l = getCompSizes(sys.argv[1],int(sys.argv[2]))
x,y=[],[]
s = set(l)
for i in s:
  x+=[i]
  y+=[l.count(i)]
  
plt.scatter(x,y)
plt.show()