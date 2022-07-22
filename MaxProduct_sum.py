import sys
 
def findMaximumProduct(A):
    if len(A) < 2:
        return
 
    max_product = -sys.maxsize
    max_i = max_j = -1
 
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if max_product < A[i] * A[j]:
                max_product = A[i] * A[j]
                (max_i, max_j) = (i, j)
    return sum([A[max_i],A[max_j]])
 
 
if _name_ == '_main_':
 
    n=int(input())
    A=list(map(int,input().split()))
    print(findMaximumProduct(A))
