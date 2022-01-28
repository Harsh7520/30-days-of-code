n = int(input())
k = int(input())
a = list(map(int, input().split()))
item = a[0]
cumu = []
for i in range(len(a)):
    if i!=0:
        item+=a[i]
        cumu.append(item)
    else:
        cumu.append(a[i])
for i in range(len(cumu)):
    if cumu[i]<=k:
        continue
    else:
        temp = i-1
        break
print(temp)
