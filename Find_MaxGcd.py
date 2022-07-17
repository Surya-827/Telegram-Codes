
def gcd(a,b):
  if b==0:return a 
  else: return gcd(b,a%b)
  
def FindMaxGCD(arr: List[int],n : int) -> int
  maxGCD = 0
  
  for i in range(n-1):
    val = gcd(arr[i],arr[i+1])
    if(val > maxGCD):
      maxGCD = val 
  return maxGCD


arr = list(map(int,input().split())
n = len(arr)
           
print(FindMaxGCD(arr,n))
