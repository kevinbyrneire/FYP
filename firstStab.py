import os, sys, zlib,time

def get_opt_string_size(stringSize,fileSize):
  return stringSize+(fileSize%stringSize)/(fileSize/stringSize)



def compressRegions(filename,min_string):
  f = open(filename)

  file_length = os.path.getsize(filename)
  min_string=get_opt_string_size(min_string,file_length)
  i=0
  dic = {}

  while file_length-i>=min_string: # build dictionary containing positions in the original file with their compressed size

    x = zlib.compress(f.read(min_string))
    dic[i] = len(x)
    i=f.tell()

  f.close()
  return dic




def organiseRegions(dic, regions):
  low = min(dic.values())
  hi = max(dic.values())
  l=[]	# organize compressed strings into regions of similarity
  m = hi-low
  l+=[low+(m/float(regions))*i for i in range(regions+1)]

  sims={}


  for k in range(len(l)-1):
    comp_range = str(k)#str(l[k])+' - '+str(l[k+1])
    sims[comp_range]=[]
    for j in dic.keys():    
      if dic[j]>=l[k] and dic[j]<l[k+1]:
        sims[comp_range]+=[j]
  return sims



def printMaxMinStrings(filename, stringSize):
  dic = compressRegions(filename, stringSize)
  hi, low = max(dic.values()), min(dic.values())
  f = open(filename)
  for i in dic.keys():
    if dic[i]==low or dic[i]==hi:
      f.seek(i)
      print f.read(stringSize)
      print
  f.close()
  return

def writeResultsToFile(dic):
  f = open('neighbourRegionsResults.csv','wb')
  low,hi=256,0
  for i in sorted(dic.keys()):
    x=len(dic[i])
    f.write(i+','+str(x)+'\n')
    if x>hi: hi=x
    elif x<low:low=x
  f.close()
  print hi-low
  return

def main():

  regions=10
  min_string = 256
  filename = sys.argv[1]

  t= time.time()
  sims = organiseRegions(compressRegions(filename,min_string), regions)
  print 'Time taken =',time.time()-t

  print 'String size =', get_opt_string_size(min_string,os.path.getsize(filename))
  #for i in sorted(sims.keys()):
    #print i+': ',sims[i] 

#printMaxMinStrings(sys.argv[1],256)
writeResultsToFile(organiseRegions(compressRegions(sys.argv[1],8192),25))
