def minPoint(input1,input2):
  a,b,c = set(),set(),set()
  
  for i in range input2:
    for j in range(i[0],i[1]+1):
      if i==input2[0]:
        a.add(j)
      elif i==input2[1]:
        b.add(j)
      else:
        c.add(j)
        
  d = []
  if(a.intersection(b,c)):
    d.append(a.intersection(b,c))
  elif(a.intersection(b)):
    d.append(a.intersection(b))
  return  len(d)

input1 = 3
input2 = []
for i in range(input1):
  input2.append(list(map(int,input().split())))
  
print(minPoint(input1,input2))
