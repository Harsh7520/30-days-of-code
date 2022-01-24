n = int(input())
k = int(input())
a = list(map(int,input().split()))
c = []

for i in range(n-k+1):
    b = a[i:i+k]
    c.append(sum(b))
print(max(c))

