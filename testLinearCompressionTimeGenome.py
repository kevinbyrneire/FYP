import time, zlib
f=open('chr1.fa')

t =time.time()

for i in range(100000):
  zlib.compress(f.read(2048))
  f.seek(i+1)

t=time.time()-t

print t

t=time.time()
f.seek(0)
s = f.read(100000)
for i in range(len(s)-2048):
  zlib.compress(s[i:i+2048])

t=time.time()-t
print t
f.close()
