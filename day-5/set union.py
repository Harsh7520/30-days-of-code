n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
set_a = set(a)
set_b = set(b)
c = set_a.union(set_b)
print(len(c))
