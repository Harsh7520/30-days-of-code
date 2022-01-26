n = int(input())
m = int(input())
matrix = []
for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)
row_lst = []
for item in matrix:
    mini = min(item)
    row_lst.append(mini)
column_lst = []
matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for item in matrix:
    maxi = max(item)
    column_lst.append(maxi)
fin = []
for i in range(n):
    for j in range(m):
        if(row_lst[i]==column_lst[j]):
            fin.append(row_lst[i])
print(*fin)
