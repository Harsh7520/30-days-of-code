m = int(input())
n = int(input())
matrix = []
b = False
for i in range(m):
        matrix.append(list(map(int,input().split())))
for i in range(len(matrix[0])):
  if(matrix[0][i]==0):
      b = True
for i in range(m):
    for j in range(n):
        if(matrix[i][j]==0):
            matrix[0][j] = 0
            matrix[i][0] = 0
for i in range(1,m):
    for j in range(n-1,-1,-1):
        if(matrix[i][0] ==0 or matrix[0][j]==0):
            matrix[i][j]=0
if(b):
    matrix[0]=[0]*n
for item in matrix:
    print(*item)
