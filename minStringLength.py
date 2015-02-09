from lzwReWrite import compress
import string, sys,random as rand
import matplotlib.pyplot as plt
from math import log,sqrt

#f=open(sys.argv[1])
#s=f.read(1000)
l=string.printable
s=''
for j in range(1000):
  s+=l[rand.randrange(len(l))]
res,x = [],[]

for i in range(1,256):
  res+=[compress(s[:i])]
  x+=[i]
  
#f.close()

#plt.plot(x,x,'red',label='linear')
#plt.plot(x,res, label='random')
plt.plot(x,[x[i]/float(res[i]) for i in range(len(x))], label='random')


plt.xlabel('Uncompressed String Length')
plt.ylabel('Compression ratio')

plt.legend(bbox_to_anchor=(0.3,0.9))

plt.show()