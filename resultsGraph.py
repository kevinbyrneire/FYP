from varyGraphCopy import getCompSizes
import numpy as np
import matplotlib.pyplot as plt
import sys, time
def main():
  t=time.time()
  l = getCompSizes(sys.argv[1],int(sys.argv[2]))
  t=time.time()-t
  plt.plot(np.arange(len(l)),l,marker=u'.')
  plt.show()
  print t
  return

main()