

import re

prompt = input("Enter here : ")

res = re.search(r'\D',prompt).start()

out = prompt[res]

nums = [ int(x) for x in prompt.split(out)]

d = { 

           '+' : nums[0] + nums[1],

           '-' : nums[0] - nums[1],

           '*' : nums[0] * nums[1],

           '/' : nums[0] / nums[1]

       }

print("Res :",res)

print("out : ",out)

print("nums : ",nums)

print(d[out])
