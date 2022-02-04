rK = input()
rV = input()
n = int(input())
c = 0
for _ in range(n):
    str1 = input()
    lst = str1.split(" ")
    if rK == "type":
        if rV == lst[0]:
            c+=1
    elif rK == "color":
        if rV == lst[1]:
            c+=1
    else:
        if rV == lst[2]:
            c+=1
print(c)
