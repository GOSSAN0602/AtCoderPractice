item=list(map(int,input().split()))
item.sort()
times=0
while sum(item)/3!=item[0]:
  if item[1]==item[2]:
    item[0]+=2
    times+=1
    item.sort()
  else:
    item[0]+=1
    item[1]+=1
    times+=1
    item.sort()
print(times)
