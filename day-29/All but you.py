n = int(input())
a = list(map(int, input().split()))
ma = max(a)
mi = min(a)
cm = a.count(ma)
ci = a.count(mi)
s_a = set(a)
if(len(s_a)==1):
    print(0)
else:
    print(len(a)-cm - ci)
