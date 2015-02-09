from lzwReWrite import compress
import string, sys,random as rand
import matplotlib.pyplot as plt
from math import log,sqrt

f=open('englishText.txt')
g=open('genome.fa')

r,s,h ='&d','aa', 'ac'

compRand, compUni, genome, x = [],[],[],[]
l=string.printable
maxString = int(sys.argv[1])

for i in range(1,int(log(maxString,2))):
  s+=f.read(2**i)
  h+=g.read(2**i)
  for j in range(2**i):
    r+=l[rand.randrange(len(l))]    

  compUni+=[compress(s)]
  compRand+=[compress(r)]
  genome+=[compress(h)]
  x+=[len(s)]
  
f.close()
g.close()

plt.plot(x, [float(x[i])/genome[i] for i in range(len(x))], label = 'genome')
plt.plot(x,[float(x[i])/compUni[i] for i in range(len(x))],label='average')
plt.plot(x,[float(x[i])/compRand[i] for i in range(len(x))],label='random')
#plt.plot(x,[sqrt(n/2) for n in x],label='best case')
#plt.plot(x,map(lambda z: sqrt(2*z),x), label='uniform')

plt.xlabel('String Length')
plt.ylabel('Compression Ratio')

plt.legend(bbox_to_anchor=(0.3,0.9))

plt.show()