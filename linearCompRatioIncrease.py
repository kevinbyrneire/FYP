from lzwReWrite import compress
import sys
import matplotlib.pyplot as plt

f = open(sys.argv[1])
s=f.read(2)
y=[]

for i in range(10000):
  s+=f.read(1)
  y+=[len(s)/float(compress(s))]
  
f.close()

plt.plot(y)
plt.show()