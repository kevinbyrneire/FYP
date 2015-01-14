from lzwReWrite import compress
import string, sys,random as rand
import matplotlib.pyplot as plt
from math import log

r,s='&d','aa'
compRand, compUni, x = [],[],[]
l=string.printable

for i in range(1,12):
  s+=2**i*'a'
  for j in range(2**i):
    r+=l[rand.randrange(len(l))]
    

  compUni+=[compress(s)]
  compRand+=[compress(r)]
  x+=[len(s)]
  
plt.plot(x,compUni,label='uniform')
plt.plot(x,compRand,label='random')
plt.plot(x,x,label='linear')
#plt.plot(x,map(lambda z: log(z,2),x))
plt.show()