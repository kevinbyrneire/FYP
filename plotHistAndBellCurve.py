import matplotlib.pyplot as plt
from getStats import *
from varyGraph import getCompSizes
import matplotlib.mlab as mlab
import sys,math

l = getCompSizes(sys.argv[1],int(sys.argv[2]))
n, bins, patches = plt.hist(l,50,normed=True)
#y = mlab.normpdf(bins, mean(l),deviation(l))

plt.xlabel('Compressed string length')

#plt.plot(bins, y, 'r')
plt.show()