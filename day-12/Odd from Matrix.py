m = int(input())
n = int(input())
ind = int(input())
indices = list(map(int,input().split()))
first_lst = []
for i in range(len(indices)-2):
    first = indices[i:i+4:2]
    first_lst.append(first)
arr=[[0]*n for _ in range(m)]
for row,col in first_lst:
    for i in range(n):
        arr[row][i]+=1
    for i in range(m):
        arr[i][col]+=1
print( sum(1 for i in range(m) for j in range(n) if arr[i][j]%2!=0))
