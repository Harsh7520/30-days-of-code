n = int(input())
matrix = []
sum = 0
for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)
for i in range(n):
    for j in range(n):
        if(i==j):
            sum += matrix[i][j]
for i in range(n):
    for j in range(n):
        if((i+j)==(n-1)):
            sum += matrix[i][j]
if(n%2!=0):
    sum -= matrix[n//2][n//2]
print(sum)
