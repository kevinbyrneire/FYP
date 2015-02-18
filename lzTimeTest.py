import time,string, random as r
from lz78 import compress
import matplotlib.pyplot as plt
from math import log

l=string.printable
f=''
res=[]


for i in range(1000):  # initialize f to a 1000 letter string
  f+=l[r.randrange(len(l))]

x=[]
  
for i in range(12):
  for j in range(2**i*1000):
    f+=l[r.randrange(0,len(l))]

  x+=[2**i*1000]
  t = time.time()
  compress(f)
  t=time.time()-t
  res+=[t]

plt.plot(x,res)
plt.ylabel('Time')
plt.xlabel('String Length')
#plt.plot(range(len(res)),map(lambda z: log(z,2),res))
plt.show()  