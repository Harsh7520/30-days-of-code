n = int(input())
a = list(map(int,input().split()))
set_a = set(a)
lst_set = list(set_a)
lst_set.sort(reverse=True)
dic = {}
for i in range(len(lst_set)):
    dic[lst_set[i]] = i
ans = []
for item in a:
    ans.append(dic[item])
print(*ans)
