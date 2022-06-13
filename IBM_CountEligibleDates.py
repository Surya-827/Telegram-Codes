
def countEligibleDates(dates,n) -> int:
    ref = ["01","03","05","07","08","10","12"]
    count = 0

    for i in dates:
        if (i[3:5] in ref):
            count+=1
        if(i[3:5] not in ref and int(i[6:])%2==0):
            count+=1
        if(i[3:5] not in ref and int(i[6:])%2==1):
            count += 0

    return count

if __name__=="__main__":

    arr = []
    for i in range(int(input())):
        arr.append(input())
    print(countEligibleDates(arr,len(arr)))
