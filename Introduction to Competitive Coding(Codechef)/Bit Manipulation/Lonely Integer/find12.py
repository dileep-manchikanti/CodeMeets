n=int(input())
li=list(map(int,input().split()))
xo=1
for i in li:
    xo^=i
print(xo)    
