
class Solution(object);

  @classmethod
  def solve(A: List[int]) -> str:
    n = len(A)
    return "%.2f" % (sum(A)//n)
  
  
 if __name__=="__main__":
  
  obj = Solution()
  A = list(map(int,input().split()))
  
  print(obj.solve(A))
  
