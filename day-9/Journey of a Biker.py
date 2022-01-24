n = int(input())
a = list(map(int, input().split()))
s = 0
sum_lst = []
sum_lst.append(s)
for i in range(len(a)):
    s += a[i]
    sum_lst.append(s)
print(max(sum_lst))
