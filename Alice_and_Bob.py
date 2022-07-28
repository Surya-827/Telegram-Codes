





import math

a = input('').split(' ')

b = input('').split(' ')

alice=bob=0

for i in range(3):

  if a[i] != b[i]:

    if a[i] > b[i]:

      alice+=1

    elif a[i] < b[i]:

      bob+=1

print(alice,bob)
