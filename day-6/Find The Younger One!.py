n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
       if(a[i]>a[j]):
           count += 1
    b.append(count)
print(*b)
