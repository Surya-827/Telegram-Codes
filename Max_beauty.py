import math

n = int(input())

a = []

for i in range(n):

    a.append(int(input()))

ans = 0

for j in range(1, 1 << n):

    index = 0

    k = []

    while(j != 0):

        if (j & 1) == 1:

            k.append(a[index])

        index += 1

        j = j >> 1

    s = sum(k)

    r = k[0]

    for p in range(1, len(k)):

        r = r | k[p]

    m = (s/r)

    ans = max(ans, m)

print(math.floor(ans*10000))

Max beauty
