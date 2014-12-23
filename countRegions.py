from firstStab import compressRegions, organiseRegions
import sys
def getCounts(filename, regions, stringSize):
  f = open(filename[:4]+'RegionCount.csv','wb')
  dic = organiseRegions(compressRegions(filename, stringSize), regions)
  s=''
  for i in dic.keys():
    s+= i + ',' + str(len(dic[i])) + '\n'
  f.write(s)
  f.close()
  return

getCounts(sys.argv[1], 10, 256)


