n=int(input())

c=0

if n<0:

    print("wrong number")

else:

    for i in range(1,n):

        if n%i==0:

            c+=1

        if c>2:

            print("Not a Prime")

            break

    if c==1:

        n=len(str(n))

        if n==1:

            print("Single-digit Prime")

        elif n%2==0:

            print("even-digit prime")

        else:

        print("Odd-digit prime")
