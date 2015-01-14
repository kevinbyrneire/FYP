def compress(s):
  ''' Adaptation of LZW compression algorithm which returns
      the number of characters in the compressed version'''
  l= set()
  w=''
  for k in s:
    wk = w+k
    if wk in l:
      w=wk
	
    else:
      l.add(wk)
      w=k

  return len(l)
