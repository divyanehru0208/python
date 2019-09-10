a,b=map(int,input().split())
list=list(map(int,input().split()[:a]))
count=0
for i in range(0,a):
    if(list[i]==b):
        count=count+1
print(count)
