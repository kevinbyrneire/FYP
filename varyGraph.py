import sys, gzip, os, time as t
from lzwReWrite import compress

def getCompSizes(inFile,stringSize):
  f = open(inFile)

  eof = os.path.getsize(inFile)
  i=0
  l = []
  while i<1000000 and eof-i>=stringSize:
    f.seek(i)
    l+=[compress(f.read(stringSize))]

    i+=1
    
  f.close()
  return l
  

def main(filename, stringsize):
  sizeList = getCompSizes(filename, stringsize)

  s=''
  for i in range(len(sizeList)):
    s+= str(i) + ',' + str(sizeList[i]) + '\n'
  f=open('linearCompressionGenome'+str(stringsize)+'.csv','wb')
  f.write(s)
  f.close()

