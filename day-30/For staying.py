n = int(input())
a = list(map(int, input().split()))
a.sort()
b = False
for i in range(n):
    for j in range(i+1, n):
        if a[j] == 2*a[i]:
            b = True
            break
if b:
    print("true")
else:
    print("false")
