n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(len(a)):
    for j in range(len(a)):
        if(i<j):
            ans.append(a[i]+a[j]+(i-j))
print(max(ans))
