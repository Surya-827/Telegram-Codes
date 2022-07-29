from typing import List


def allMEX(A:List[int],N:int) -> List[int]:
  dp = [] * N
  
  if(len(set(A))==1 and 0 in set(A)):
    for i in range(N+1):
      dp.append(i)
  elif(N-1==len(set(A))):
    for i in range(0,N-1):
      dp.append(i)
  else:
    dp.append(0)
  return dp 


if __name__=="__main__":
  
  A = []
  for _ in range(int(input())):
    A.append(int(input()))
    
  N = len(A)
  result = allMEX(A,N)
  
  for i in range(len(result)):
    print(result[i])
