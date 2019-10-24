from collections import Counter
n=int(input())
a=[input() for _ in range(n)]
cnt=Counter(a)
ans=0
for i in cnt.values():
  if i%2:
    ans+=1
print(ans)
