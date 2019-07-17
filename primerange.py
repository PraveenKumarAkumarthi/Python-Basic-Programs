t,b=(map(int,input().split()))
for i in range(t+1,b):
  for x in range(2,i):
    if(i%x==0):
      break
  else:
    print(i,end=" ")   
