import math
n=int(input())
a=int(math.sqrt(n))
ans=len(str(n))
for i in range(1,a+1):
  if n%i==0:
    cand=len(str(max(i,int(n/i))))
    if ans>cand:
      ans=cand
print(ans)
