n = int(input())
c = 0
for i in range(n):
    a = list(map(int, input().split()))
    for item in a:
        if(item<0):
            c+=1
print(c)
