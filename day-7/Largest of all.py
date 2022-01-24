n = int(input())
a = list(map(int,input().split()))
max_1 = max(a)
a.remove(max_1)
max_2 = max(a)
if(max_1>2*max_2):
    print("true")
else:
    print("false")
