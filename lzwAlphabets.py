import string
import random as r
from lzwReWrite import compress
import matplotlib.pyplot as plt

stringlength = 100000
l=string.printable
res=[]
for i in range(1,21):
  f=''
  x=i*(len(l)//20)
  for j in range(stringlength):    
    f+=l[r.randrange(x)]
	
  res+=[stringlength/float(compress(f))]
plt.plot(range(len(res)),res)
plt.show()
  #s = open('textFile'+str(x)+'.txt','w')
  #s.write(f)
  #s.close()

