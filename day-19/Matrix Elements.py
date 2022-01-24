n = int(input())
matrix = []
a = []
bool = False
for i in range(n):
    a.append(i+1)
    matrix.append(list(map(int,input().split())))
set_a = set(a)
for item in matrix:
    s_item = set(item)
    if(len(s_item)==len(set_a)):
        bool = True
    else:
        bool = False
        break
trans = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for item in trans:
    s_item = set(item)
    if (len(s_item) == len(set_a)):
        bool = True
    else:
        bool = False
        break
if(bool):
    print("true")
else:
    print("false")
