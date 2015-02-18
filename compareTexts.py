import sys
from getStats import *
from varyGraph import getCompSizes
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

stringSize=int(sys.argv[1])
l = getCompSizes('englishText.txt', stringSize)
n = getCompSizes('spanishText.txt', stringSize)

m, bins, p = plt.hist(l,50,normed=True,visible=False)
m1, bins1, p1 = plt.hist(n,50,normed=True,visible=False)

y = mlab.normpdf(bins, mean(l),deviation(l))
y1 = mlab.normpdf(bins1, mean(n),deviation(n))

plt.plot(bins,y,label='English')
plt.plot(bins1,y1,'b--',label='Spanish')

plt.xlabel('Compressed Size')
plt.legend()
plt.show()