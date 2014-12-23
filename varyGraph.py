import sys, gzip, os, time as t, zlib


def getCompSizes(inFile,stringSize):
  f = open(inFile)
  #text = f.read()
  #f.close()
  eof = os.path.getsize(inFile)
  i=0
  l = []
  
  while i<1000000 and eof-i>=stringSize:

    x = zlib.compress(f.read(stringSize))

    l+=[len(x)]
    i+=1
    f.seek(i)
  return l

def main(filename, stringsize):
  sizeList = getCompSizes(filename, stringsize)

  s=''
  for i in range(len(sizeList)):
    s+= str(i) + ',' + str(sizeList[i]) + '\n'
  f=open('linearCompressionGenome'+str(stringsize)+'.csv','wb')
  f.write(s)
  f.close()

for i in range(8,15):
  main(sys.argv[1],2**i)
#main(sys.argv[1], int(sys.argv[2]))
