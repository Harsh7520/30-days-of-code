n = int(input())
k = int(input())
a = list(map(int,input().split()))
temp = (n-1)*k
s = sum(a)
ele = s - temp
if ele in a:
    print("true")
else:
    print("false")
