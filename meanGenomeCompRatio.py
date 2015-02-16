from varyGraph import getCompSizes
import matplotlib.pyplot as plt
from getStats import mean
x,res=[],[]
for i in range(1,100):
  l = getCompSizes('genome.fa',i)
  print i,mean(l)
  res+=[i/mean(l)]
  x+=[i]
  
plt.plot(x,res)

plt.ylabel('Mean Compression Rate')
plt.xlabel('String Length')
plt.show()