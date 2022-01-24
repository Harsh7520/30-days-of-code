n = int(input())
matrix = []
for i in range(n):
    a = list(map(int,input().split()))
    a.reverse()
    for i in range(len(a)):
        a[i] = 0 if a[i] else 1
    matrix.append(a)
for i in matrix:
    print(*i)
