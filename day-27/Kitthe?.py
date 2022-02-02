n = int(input())
k = int(input())
a = list(map(int, input().split()))
try:
    print(a.index(k))
except:
    print("-1")
