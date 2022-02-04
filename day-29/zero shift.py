n = int(input())
a = list(map(int, input().split()))
a_c = a.count(0)
for i in range(a_c):
    a.remove(0)
for i in range(a_c):
    a.append(0)
print(*a)
