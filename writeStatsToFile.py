import sys
from getStats import deviation
from varyGraph import getCompSizes

f = open('standardDeviations.csv','a')
for i in range(2,8):
  f.write(str(i) + ',' + str(deviation(getCompSizes(sys.argv[1],2**i)))+'\n')
f.close()
