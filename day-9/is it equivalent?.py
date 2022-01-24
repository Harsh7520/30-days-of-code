n = int(input())
a = list(map(int, input().split()))
s_a = set(a)
bool = False
for i in s_a:
    c = a.count(i)
    if c==i:
        bool = True
if(bool):
    print("true")
else:
    print("false")
