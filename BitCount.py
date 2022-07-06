
class Solution(object):
    @classmethod
    def getCount(cls,a:int,b:int) -> int:
        res = a * b
        t = bin(res)
        return str(t).lstrip("ob").count("1")


if __name__=="__main__":
    x = int(input())
    y = int(input())
    obj  = Solution()
    print(obj.getCount(x,y))