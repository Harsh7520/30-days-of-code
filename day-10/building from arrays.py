n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    b.append(a[a[i]])
print(*b)
