from lz78 import compress
import string, sys,random as rand
import matplotlib.pyplot as plt
from math import log,sqrt

f=open('englishText.txt')
r,s='&d','aa'
compRand, compUni, x = [],[],[]
l=string.printable
maxString = int(sys.argv[1])

for i in range(1,int(log(maxString,2))):
  s+=f.read(2**i)

  for j in range(2**i):
    r+=l[rand.randrange(len(l))]    

  compUni+=[compress(s)]
  compRand+=[compress(r)]
  x+=[len(s)]
  
f.close()

plt.plot(x,compUni,'g--',	label='average')
plt.plot(x,compRand,'b-.',label='random')
plt.plot(x,x,label='linear',color='red')
plt.plot(x,map(lambda z: sqrt(2*z),x), 'k:',label='optimal',markersize=20)

plt.xlabel('Uncompressed String Length')
plt.ylabel('Compressed Length')

plt.legend(bbox_to_anchor=(0.3,0.9))

plt.show()