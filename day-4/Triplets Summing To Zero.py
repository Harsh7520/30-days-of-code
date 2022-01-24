import itertools
n = int(input())
a = list(map(int,input().split()))
bool = False
combs = list(itertools.combinations(a,3))
for i in combs:
    s = sum(i)
    if(s==0):
        bool = True
        break
    else:
        bool = False
if(bool == True):
    print("true")
else:
    print("false")
