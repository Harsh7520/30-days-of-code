n = int(input())
a = list(map(int,input().split()))
area = []
for i in range(len(a)):
    for j in range(i,len(a)):
        h = min(a[i],a[j])
        w = j-i
        ar = h*w
        area.append(ar)
print(max(area))
