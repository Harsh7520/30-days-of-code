n = int(input())
a = list(map(int,input().split()))
ind = []
for i in range(len(a)):
    if((i==0 and a[i]>a[i+1]) or (a[i]>a[i-1] and i==n-1) or (a[i-1]<a[i]>a[i+1])):
        ind.append(i)
print(*ind)
