from varyGraphCopy import getCompSizes
import numpy as np
import matplotlib.pyplot as plt
import sys, time
from getStats import *
def main():
  t=time.time()
  l = getCompSizes(sys.argv[1],int(sys.argv[2]))
  t=time.time()-t
  
  plt.plot(np.arange(len(l)),l,'green')#,marker=u'.')
  plt.plot(len(l)*[mean(l)],label='mean')
  plt.plot(len(l)*[median(l)], 'r--',label='median')
  plt.legend()
  plt.ylabel('Compressed Size')
  plt.xlabel('Position')
  plt.show()
  print t
  return

main()