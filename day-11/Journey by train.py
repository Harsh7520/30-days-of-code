n = int(input())
lst_a = []

ans_lst = []
for _ in range(n):
    a = list(map(int, input().split()))
    sta = a[0]
    sto = a[1]
    val = a[2]
    b = [0]*(a[0]-1)
    for i in range(sta,sto+1):
        b.append(val)
    lst_a.append(b)

num = int(input())
for i in lst_a:
    for j in range(num-len(i)):
        i.append(0)

for i in range(num):
    ans = 0
    for j in range(n):
        ans = ans + lst_a[j][i]

    ans_lst.append(ans)

print(*ans_lst)
