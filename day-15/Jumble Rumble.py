n = int(input())
a = list(map(int, input().split()))
f_l = a[:n]
s_l = a[n:]
ans = []
for i in range(n):
    ans.append(f_l[i])
    ans.append(s_l[i])
print(*ans)
