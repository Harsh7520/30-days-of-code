n = int(input())
matrix = []
for i in range(n):
    s = input()
    lst = list(s)
    matrix.append(lst)

result = [[] for _ in range(max(len(sl) for sl in matrix))]

for sl in matrix:
    for x, res_sl in zip(sl, result):
        res_sl.append(x)
if(matrix==result):
    print("true")
else:
    print("false")
