n = int(input())
a = list(map(int, input().split()))
dest = n-1
for i in range(len(a))[::-1]:
    if(i+a[i]>=dest):
        dest = i
if(not(dest)):
    print("true")
else:
    print("false")
