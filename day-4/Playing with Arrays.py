n = int(input())
a = list(map(int,input().split()))
ans = []
s = 0
for i in a:
    s += i
    ans.append(s)
print(*ans)
