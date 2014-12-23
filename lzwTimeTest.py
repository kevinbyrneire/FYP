import time
import zlib
import string
import random as r
l=string.printable
f=''
for i in range(1000):  # initialize f to a 1000 letter string
  f+=l[r.randrange(len(l))]

for i in range(12):
  for j in range(2**i*1000):
    f+=l[r.randrange(0,len(l))]

  t = time.time()
  zlib.compress(f)
  t=time.time()-t
  print(len(f),t)
