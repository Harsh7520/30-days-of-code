n = int(input())
a = list(map(int,input().split()))
b = a.copy()
ans = []
for i in range(len(a)):
    b.remove(a[i])
    mul = 1
    for j in range(len(b)):
        mul = mul*b[j]
    ans.append(mul)
    b.insert(i,a[i])
print(*ans)
