import os
f=open('fileSizes.csv','w')
x=''
for i in range(1,21):
  x+=str(5*i)+','+str(os.path.getsize('textFile'+str(5*i)+'.txt.gz'))+'\n'
print(x)
f.write(x)
f.close()
