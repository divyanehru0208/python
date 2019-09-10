num=int(input())
mylist=list(map(int,input().split()))
Max=-65535
Min=65538
for i in range(0,num):
    if(mylist[i]<Min):
            Min=mylist[i]
            a=i
    if(mylist[i]>Max):
            Max=mylist[i]
            b=i
print(a+1,b+1)

            
            

