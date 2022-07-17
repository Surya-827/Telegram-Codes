
import sys as s 

class Solution(object):
  
  @classmethod
  def getmaxDiff(cls, A : List[int]) -> int:
    diff = -s.maxsize
    n = len(A)
    
    if n==0:return diff 
    
    for i in range(n-1):
      for j in range(i+1,n):
        if(A[j] > A[i]):
          diff = max(digg,A[j]-A[i])
    return diff 
  
  
  
 if __name__=="__main__":
    obj = Solution()
    siz = int(input())
    A = list(map(int,input().split())) [ : siz] 
    
    print(obj.getMaxDiff(A))
