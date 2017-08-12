
from random import randint

def hanoi(N,M,T):
  # initially, all disks start at 0
  st=[[s for s in range(N,0,-1)]]
  for i in range(0,M-1):
    st.append([])
  weight=sum(st[0])
  for t in range(1,T+1):
  
    while True:
      # randomly select disk to move
      id=randint(1,min(N,t))
      # locate the stack 
      for j in range(len(st)):
        for i in range(len(st[j])):
          if (st[j][i]==id):
            jo=j
      
      a=st[jo][-1]
      if (jo > 0 and jo < M-1):
        if (len(st[jo+1])==0):
          b=N+1
        else:
          b=st[jo+1][-1]
        flag1=check(a,b)
        if (len(st[jo-1])==0):
          c=N+1
        else:
          c=st[jo-1][-1]
        flag2=check(a,c)
        
        if (flag1*flag2<0):
          if (flag1==-1):
            j=jo-1
          else:
            j=jo+1
          break
        elif (flag1*flag2>0 and flag1==1):
          x=randint(0,1)
          if (x==1):
            j=jo+1
          else:
            j=jo-1
          break
      elif (jo==0):
        if (len(st[jo+1])==0):
          b=N+1
        else:
          b=st[jo+1][-1]
        flag1=check(a,b)
        if (flag1==1):
          j=jo+1
          break
      elif (jo==M-1):
        if (len(st[jo-1])==0):
          b=N+1
        else:
          b=st[jo-1][-1]
        flag1=check(a,b)
        if (flag1==1):
          j=jo-1
          break

    a=st[jo].pop()
    st[j].append(a)
  #  print(st)
  m=0
  for j in range(len(st)):
    for i in range(len(st[j])):
      m=m+st[j][i]*j
  a=m/weight
  return a




def check(new,top):
  if (new > top):
    # not valid
    flag=-1
  else:
    flag=1
  return flag


import numpy
arr=[]
for i in range(1000):
  #a=hanoi(3,3,16)
  a=hanoi(6,6,256)
  arr.append(a)
print(numpy.mean(arr))
print(numpy.std(arr, axis=0))

#0.440333333
#0.264986163

#1.366714285
#0.502712819
