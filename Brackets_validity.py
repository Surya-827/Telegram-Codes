left =[ '(' , '[' , '{' ]

right = [ ')' , ']' , '}' ]

Dp =dict(zip(right , left))

for _ in range(int(input())):

    New=[]

    for x in input():

         if New and Dp[x] ==New[-1]:

               New.pop()

         else:

               New.append(x)

     print(*[ "error" if New else "correct" ])

Python3 ✅🤞🙂
