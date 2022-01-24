n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if (-i in a):
        b.append(i)
if(b == []):
    print(-1)
else:
    print(max(b))
