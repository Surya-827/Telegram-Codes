"""
INPUT :
N : Number of Elements
Arr :  List of Elements [n]
Target = 23
t = Limit elements

OUTPUT :
x + y + z if t==3 and sum(x,y,z) ==Target

"""

n = 10
arr = [12,-1,0,7,3,11,9,7,4,10][:n]
Target = 23
#
# for i in range(n):
#     k = arr.pop()
#     TarK = Target - k
#     if(arr[i]+arr[i+1]<=TarK):
#         flag = True
#
#
from itertools import permutations as  p
import random as r

r.shuffle(arr)
print(arr)