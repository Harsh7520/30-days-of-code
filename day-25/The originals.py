n = int(input())
a = list(map(int, input().split()))
set_a = set(a)
b = False
new_lst = []
for item in set_a:
    count = a.count(item)
    if count not in new_lst:
        new_lst.append(count)
    else:
        b = True
        break
if b==False:
    print("true")
else:
    print("false")
