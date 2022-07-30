
class Solution(object):

	@classmethod
	def isAnagram(cls, str1 : str, str2 : str) -> bool:

		if(sorted(list(str1)) == sorted(list(str2))):
			return True
		return False


	@classmethod
	def getResult(cls, value : bool) -> str:

		if(value==-1):
			return "Yes"
        return "No"


 if __name__=="__main__":

 	obj = Solution()
 	x,y =  map(str,input().split(","))

 	print(obj.getResult(obj.isAnagram(x,y)))
