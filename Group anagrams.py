from typing import List

class Solution(object):

    @classmethod

    def groupAnagrams(cls,s: List[str]) -> List[List[str]]:

        d = dict()

        for ele in s:

            temp = ''.join(sorted(ele))

            if temp in d:

                d[temp].append(ele)

            else:

                d[temp] = [ele]

        res =[]

        for val in d.values():

            res.append(val)

        ans = sorted(res, key=lambda x : len(x))

        return ans

        

if __name__=="__main__":

    obj = Solution()

    s = list(map(str,input().split()))

    print(obj.groupAnagrams(s))
