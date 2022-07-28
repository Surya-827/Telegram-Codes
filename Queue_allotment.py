Queue allotment in python 

for _ in range(int(input())):

    n,m,k,l = map(int, input().split())

    a = list(map(int, input().split()))

    a = sorted(a)

    time = m*l+l

    min = time - a[0]

    time += l

    for i in range(1,n):

        if time - a[i] < min:

            min = time - a[i]

        time += l

    if min > time - k:

        min = time -k

    print(min)
