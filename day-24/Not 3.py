n = int(input())
a = list(map(int, input().split()))
set_a = set(a)
for i in set_a:
    if a.count(i)==1:
        print(i)
        break
