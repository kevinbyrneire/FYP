import string
import gzip
import random as r
l=string.printable
for i in range(1,21):
  f=''
  for j in range(2**11*1000):
    x=i*(len(l)//20)
    
    f+=l[r.randrange(x)]
  print(i,x)
  s = open('textFile'+str(x)+'.txt','w')
  s.write(f)
  s.close()

