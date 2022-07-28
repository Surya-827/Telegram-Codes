a=list(map(int,input().split()))
k=a[1]
count=0
co=0
for i in range(1,a[0]+1):
    s=str(bin(i))
    s=s[2:len(s)]
    count=0
    while "101" in s:
        h=s.index("101")
        s=s[h+2:]
        count+=1
        if count>=k:
            co+=1
            break
print(co)




#python 3 ✅ very cool number
