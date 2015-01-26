import string
import random as r
from lzwReWrite import compress
import matplotlib.pyplot as plt
from math import log

stringlength = 10000
l=string.printable
xaxis = []
res=[]
for i in range(1,21):
  f=''
  x=i*(len(l)//20)
  xaxis+=[x]
  for j in range(stringlength):    
    f+=l[r.randrange(x)]
	
  res+=[stringlength/float(compress(f))]
plt.plot(xaxis,res)
plt.xlabel('Alphabet Size')
plt.ylabel('Compression Ratio')
#plt.yscale('log')
plt.show()


