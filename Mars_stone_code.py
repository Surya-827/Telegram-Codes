def maxUnique(input1,input2,input3):

    l=list(range(1,input1+1))

    for i in input3:

        l.remove(i)

    #print(l)

    l.sort()

    summ=0

    count=0

    for i in l:

        summ+=i

        if(summ<=input1):

            count+=1

        else:

            break

    return count

























                





