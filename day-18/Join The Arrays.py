n = int(input())
a = list(map(int,input().split()))
b = a
b.extend(a)
print(*b)
