n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = False
for i in range(n):
    for j in range(1,n):
        if(b==True):
            break
        if(a[i]+a[j]==m and i!=j):
            b = True
            print("true")
            break
if(b==False):
    print("false")
