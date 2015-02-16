from lzwReWrite import compress
import string, sys,random as rand
import matplotlib.pyplot as plt
from math import log,sqrt

g=open('genome.fa')

r='ac'

genome, x = [],[]

maxString = int(sys.argv[1])

for i in range(1,maxString):

  r+=g.read(1)  
  genome+=[compress(r)]
  x+=[len(r)]
  

g.close()

plt.plot(x, [float(x[i])/genome[i] for i in range(len(x))], label = 'genome')

#plt.plot(x,[sqrt(n/2) for n in x],label='uniform')


plt.xlabel('String Length')
plt.ylabel('Compression Ratio')

plt.legend(bbox_to_anchor=(0.3,0.9))

plt.show()