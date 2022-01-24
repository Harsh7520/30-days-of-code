n = int(input())
a = list(map(int,input().split()))
t = int(input())
b = False
for i in range(len(a)):
    if(a[i]>t):
        print(a[i])
        b = True
        break
if(b==False):
    print("-1")
