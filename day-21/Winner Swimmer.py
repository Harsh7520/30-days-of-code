n = int(input())
a = list(map(int,input().split()))
ans = 0
a.sort()
an = 0
for i in range(n - 1, -1, -1):
    cand = a[i] + n - i
    if cand > an:
        an = cand
for j in a:
    if j + n >= an:
        ans += 1
print(ans)
