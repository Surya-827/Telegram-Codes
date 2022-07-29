def constructPrintLIS(N, x):
 l = [[] for i in range(N)]
 l[0].append(x[0])
 for i in range(1, N):
  for j in range(i):
   if x[i] >= x[j] and (len(l[i]) < len(l[j]) + 1):
    l[i] = l[j].copy()
  l[i].append(x[i])
 maxx = l[0]
 for x in l:
  if len(x) > len(maxx):
   maxx = x
 res = 0
 for i in range(len(maxx)):
  res += maxx[i]*maxx[i]*maxx[i]
 return res

if __name__ == "__main__":

 arr = list(map(int,input().split()))
 n = len(arr)

 print(constructPrintLIS(n, arr))
