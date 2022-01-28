n = int(input())
m = int(input())
matrix = []
b = True
for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)

i = 0
j = 0
ele = matrix[i][j]
while(i<n and j<m):
    if(matrix[i][j]!=ele):
        b = False
    i+=1
    j+=1
if(b):
    print("true")
else:
    print("false")
