class Solution(object):
    
    def isLeap(self,n:int) -> bool:
        if((n%400==0) or (n%100!=0) and (n%4==0)):
            return True
        return False
    
    def getSolve(self, y:int) -> str:
        cal = [31,28,31,30,31,30,31,31,30,31,30,31]
        prog = 8
        
        if(self.isLeap(y)==-1):
            cal[1]+=1
        else:
            cal[1]+=0 
        till_date = cal[:8]
        curr_date = 256 - sum(till_date)
        
        return f"{curr_date}.{str(prog+1).zfill(2)}.{y}"

        
        
        
if __name__=="__main__":
    
    obj = Solution()
    y = int(input())
    print(obj.getSolve(y))
        
