import sys
from getStats import *
from varyGraphCopy import getCompSizes
import matplotlib.pyplot as plt
from bellCurve import freqDist

l = getCompSizes(sys.argv[1], int(sys.argv[2]))

left = l[:len(l)/2]
right = l[len(l)/2:]

plt.plot([i[0] for i in freqDist(left)], [i[1] for i in freqDist(left)])
plt.plot([i[0] for i in freqDist(right)], [i[1] for i in freqDist(right)])

plt.show()