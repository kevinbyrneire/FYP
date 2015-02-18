from lz78 import compress
import sys, random as rand
import matplotlib.pyplot as plt
from math import log

f=open('genome.fa')
s,r=f.read(2),'ag'
randRes, res,x = [],[],[]

alpha='agct'
maxString = int(sys.argv[1])

for i in range(1,int(log(maxString,2))):
  s+=f.read(2**i)   
  for j in range(2**i): r+=alpha[rand.randrange(4)]
  res+=[compress(s)]
  randRes+=[compress(r)]
  x+=[len(s)]
  
f.close()


plt.plot(x,x,label='linear',color='red')
plt.plot(x,res)
plt.plot(x,randRes)

plt.xlabel('Uncompressed String Length')
plt.ylabel('Compressed Length')

plt.legend(bbox_to_anchor=(0.3,0.9))

plt.show()