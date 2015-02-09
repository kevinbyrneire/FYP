import sys
from getStats import *
from varyGraphCopy import getCompSizes
import matplotlib.pyplot as plt
from bellCurve import freqDist

l = getCompSizes(sys.argv[1], int(sys.argv[3]))
r = getCompSizes(sys.argv[2], int(sys.argv[3]))


plt.plot([i[0] for i in freqDist(l)], [i[1] for i in freqDist(l)])
plt.plot([i[0] for i in freqDist(r)], [i[1] for i in freqDist(r)])

plt.show()
