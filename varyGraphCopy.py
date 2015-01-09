import sys, gzip, os, time as t, zlib
from lzwReWrite import compress

def getCompSizes(inFile,stringSize):
  f = open(inFile)

  eof = os.path.getsize(inFile)
  i=0
  l = []

  while i<10000 and eof-i>=stringSize:

    l+=[compress(f.read(stringSize))]

    i+=1
    f.seek(i)
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

#for i in range(8,15):
 # main(sys.argv[1],2**i)
#main(sys.argv[1], int(sys.argv[2]))
