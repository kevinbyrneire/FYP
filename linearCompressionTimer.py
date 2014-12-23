from varyGraph import getCompSizes
import time as t
for i in range (3,12):
  startTime = t.time()
  getCompSizes('test.log',2**i)
  print t.time() - startTime
