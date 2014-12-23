import string
import random as r
l = string.printable

for j in range(1,11):
  f = open('randomTester'+str(2**j)+'.txt','w')
  x=open('uniformTester'+str(2**j)+'.txt','w')
  for i in range(2**j):
    f.write(l[r.randrange(0,len(l))])
    x.write('A')
  f.close()
  x.close()
