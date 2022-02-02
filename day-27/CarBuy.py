n = int(input())
k = int(input())
a = list(map(int, input().split()))
a.sort()
cumu_lst = [a[0]]
s = a[0]
for i in range(1, n):
    s += a[i]
    cumu_lst.append(s)
cumu_lst.append(k)
cumu_lst.sort()
final_answer = cumu_lst.index(k)
print(final_answer)
