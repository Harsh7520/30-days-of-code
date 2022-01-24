n = int(input())

a = list(map(int, input().split()))
b = False
for i in range(len(a)):
    if(a[i]==i):
        print(i)
        b = True
        break
if b == False:
    print(-1)
