n = int(input())
a = list(input().split())
b = []
bool = False
bool_2 = True
for item in a:
    if("P" in item):
        b.append(item)
    elif("D" in item):
        item = list(item)
        item[0]="P"
        s = "".join(item)
        if(s not in b):
            bool_2 = False
            break
        else:
            b.remove(s)

if(len(b)==0):
    bool = True
if(bool and bool_2):
    print("true")
else:
    print("false")
