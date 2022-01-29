m = int(input())
n = int(input())
matrix = []
for i in range(m):
    a = list(map(int, input().split()))
    matrix.append(a)
res = [[matrix[j][i] for j in range(m)] for i in range(n)]
for i in res:
    print(*i)
