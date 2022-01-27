n = int(input())
a = list(map(int,input().split()))
ans = []
for i in a:
    if i not in ans:
        ans.append(i)
    else:
        ans.remove(i)
print(*ans)
