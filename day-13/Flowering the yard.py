n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = 0
p = 0
l = 0
for i in range(n - 1):
    if a[i] == 0 and p == 0 and a[i + 1] == 0:
        p = 1
        c += 1
    else:
        p = a[i]

if p == 0 and a[-1] == 0 and l == 0:
    p = 1
    c += 1

if c >= m:
    print("true")
else:
    print("false")
