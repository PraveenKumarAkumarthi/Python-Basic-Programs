t=int(input())

if((t<=10000)and(t>1)):
  for i in range(2,(t//2)+1):
    if((t%i==0)):
      print("no")
      break
      
  else:
    print("yes")
