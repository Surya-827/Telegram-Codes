
def maxSet(N:int) -> int:
  def fact(num:int) -> int:
    ans = 1 
    for i in range(1,num+1):
      ans*=i 
     return ans 
  
  result = 1 
  for i in range(2,N):
    if(fact(i)%N==1):
      result=i
      break
  return result 


