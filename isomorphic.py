j,k=map(str,input().split())
if(len(j)!=len(k)):
  print("no")
else:
  p=[j.count(i) for i in j]
  a=[k.count(i) for i in k]
if(p==a):
  print("yes")
else:
  print("no")
