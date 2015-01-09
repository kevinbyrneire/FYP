def compress(s):

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
