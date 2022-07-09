a = input().split(" ")

c = 0

for i in a:

    if (len(i) > c) and (len(i) % 2 == 0):

        c = len(i)

for i in a:

    if len(i) == c:

        print(i)

        break
