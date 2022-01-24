n = int(input())
k = int(input())
ans = []
for i in range(n):
    lst = list(map(int, input().split()))
    sum_lst = sum(lst)
    ans.append(sum_lst)
print(max(ans))
