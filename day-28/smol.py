c = input()
n = int(input())
a = input()
b = []
b[:0] = a
bo = False
for i in range(len(b)):
    if(b[i]>c):
        bo = True
        print(b[i])
        break
if(bo == False):
    print(b[0])
