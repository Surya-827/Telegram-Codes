from typing import List 


class Solution(object):
    
    @classmethod
    def printSeries(cls,n:int) -> List[int]:
        res = []
        
        for i in range(n+1):
            x = (5*i) + 2 
            if(x%4!=0):
                res.append(x)
        return res 
        
        
if __name__=="__main__":
    
    obj = Solution()
    n = int(input())
    ans = obj.printSeries(n)
    
    for i in ans:
        print(i)
    
