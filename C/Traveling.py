def odd_even_same(p):
  t,x,y=p[0],p[1],p[2]
  if (x+y)%2==t%2:
    return 1
  else:
    return 0
def dist_judge(p):
  t,x,y=p[0],p[1],p[2]
  if t >= x+y:
    return 1
  else:
    return 0
N=int(input())
p=[]
for i in range(N):
  p.append(list(map(int,input().split())))
for i in p:
  if odd_even_same(i)*dist_judge(i):
    pass
  else:
    print("No")
    exit()
print("Yes")
