import time,string, random as r
from lzwReWrite import compress
import matplotlib.pyplot as plt

l=string.printable
f=''
res=[]
for i in range(1000):  # initialize f to a 1000 letter string
  f+=l[r.randrange(len(l))]

for i in range(12):
  for j in range(2**i*1000):
    f+=l[r.randrange(0,len(l))]

  t = time.time()
  compress(f)
  t=time.time()-t
  res+=[t]

plt.plot(range(len(res)),res)
plt.show()  