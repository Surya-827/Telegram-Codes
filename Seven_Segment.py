
"""WAY 1"""

def getLines(n):
    sum = 0
    n = list(n)
    for d in n:
        d = int(d)
        if d == 1:
            x = 2
        elif d == 7:
            x = 3
        elif d == 4:
            x = 4
        elif d == 2 or d == 5 or d == 3:
            x = 5
        elif d == 8:
            x = 7
        elif d == 0 or d == 6 or d == 9:
            x = 6
        sum += x
    return sum


n = int(input())
for i in range(n):
    d = input()
    x = getLines(d)

    if x % 2 == 0:
        for i in range(x // 2):
            print("1", end="")
    else:
        print("7", end="")
        for i in range(x // 2 - 1):
            print("1", end="")
    print()



"""
WAY 2 
def getLineCount(num) -> int:
    sum=0
    nums = list(range(1,10))
    lines = [2,5,5,4,5,6,3,7,6]
    vals = dict(zip(nums,lines))
    num = list(num)
    for digit in num:
        digit = int(digit)
        if(digit>0):
            x=(vals.get(digit))
        sum+=x
    return sum



for _ in range(int(input())):
    x = input()
    result = getLineCount(x)
    if(result % 2 ==0):
        for i in range(result//2):
            print("1",end="")
    else:
        print("7",end="")
        for i in range(result//2 - 1):
            print("1",end="")
    print()



"""
