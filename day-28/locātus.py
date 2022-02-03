n = int(input())
t = int(input())
a = list(map(int, input().split()))
if t not in a:
    print("-1 -1")
else:
    start = a.index(t)
    a.reverse()
    stop = a.index(t)
    ans = []
    ans.append(start)
    ans.append(n-1-stop)
    print(*ans)
