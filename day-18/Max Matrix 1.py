n = int(input())
matrix = []
count = 0
for i in range(n):
    matrix.append(list(map(int,input().split())))
row_lst = []
for item in matrix:
    maximum = max(item)
    row_lst.append(maximum)
column_lsts = []
for i in range(n):
    column_lst = []
    for j in range(n):
        column = matrix[j][i]
        column_lst.append(column)
    maxi = max(column_lst)
    column_lsts.append(maxi)
for i in range(n):
    for j in range(n):
        if(matrix[i][j]==row_lst[i] and matrix[i][j]==column_lsts[i] or matrix[i][j]==row_lst[j] and matrix[i][j]==column_lsts[j]):
            count+= 1

print(count)
