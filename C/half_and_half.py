a,b,c,x,y=map(int,input().split())
p_=a*x+b*y
for i in range(10**5+1):
  p=i*2*c+a*max(0,x-i)+b*max(0,y-i)
  if p<p_:
    p_=p
print(p_)
