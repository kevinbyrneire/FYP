from varyGraphCopy import getCompSizes
import sys

def getMinString(inFile, stringSize):
  l= getCompSizes(inFile,stringSize)
  i = l.index(min(l))
  
  f=open(inFile)
  f.seek(i)
  
  s=f.read(stringSize)
  
  f.close()
  
  return s
  
def getMaxString(inFile, stringSize):
  l= getCompSizes(inFile,stringSize)
  i = l.index(max(l))
  
  f=open(inFile)
  f.seek(i)
  
  s=f.read(stringSize)
  
  f.close()
  
  return s

filename, stringSize = sys.argv[1],int(sys.argv[2])
print getMinString(filename,stringSize)
print
print getMaxString(filename, stringSize)