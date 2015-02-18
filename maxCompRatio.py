from lz78 import compress
import string
import matplotlib.pyplot as plt
from math import sqrt

s='aa'
compUni, x = [],[]
l=string.printable

for i in range(1,13):
  s+=2**i*'a'  

  compUni+=[compress(s)]
  x+=[len(s)]  


plt.plot(map(lambda z: sqrt(2*z),x),compUni)
plt.ylabel('Compressed Size')
plt.xlabel('sqrt(2n)')
plt.show()