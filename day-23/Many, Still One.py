n = int(input())
a = list(map(int, input().split()))
str_a = "".join([str(ele) for ele in a])
lf = str_a.index("1")
rf = str_a.rindex("1")
slic = str_a[lf:rf+1]
slic_lst = list(slic)
b = True
for i in range(len(slic_lst)):
    if(slic_lst[i]!='1'):
        b = False
        break
if(b):
    print("true")
else:
    print("false")
