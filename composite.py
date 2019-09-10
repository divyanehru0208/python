num=int(input())
count=0
for i in range(2,num):
    if num%i==0:
        count=count+1
        break
if count>0:
   print("yes")
else:
   print("No")
