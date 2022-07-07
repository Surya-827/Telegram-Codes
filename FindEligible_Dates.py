/Python

'''Find Eligible dates Code'''

n=int(input())

arr=[]

count=0

for x in range(n):

    temp=list(map(int,input().split("/")))

    arr.append(temp) 

    if temp[1] in [1,3,5,7,8,10,12]:

        count+=1 

if count!=0:

    print(count)

else:

    for x in arr:

        if x[2]%2==0:

            count+=1 

    print(count)

