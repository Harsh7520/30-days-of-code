m = int(input())
n = int(input())
k = int(input())
matrix = []
for i in range(m):
     a = (list(map(int,input().split())))
     matrix.extend(a)

matrix.sort()

if(k==0):
    print(matrix[0])
else:
    print(matrix[k])
