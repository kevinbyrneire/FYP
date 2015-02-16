from varyGraph import getCompSizes
import matplotlib.pyplot as plt
import sys

def freqDist(l):

  x,y=[],[]
  s = set(l)
  for i in s:
    x+=[i]
    y+=[l.count(i)]
  
  return zip(x,y)
  
  
def writeToFile(l):
  f = open('FreqAnalysis.csv','w')
  for i in l:
    f.write(str(i[0]) + ',' + str(i[1]) + '\n')
  f.close()
  return
  
#l = getCompSizes(sys.argv[1],int(sys.argv[2]))
#writeToFile(main(l))