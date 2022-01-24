n,k = map(int,input().split())
lst = list(map(int,input().split()))
lst_set = set(lst)
c = 0
flr = n//k
for i in lst_set:
    if(lst.count(i) == flr):
        c += 1
print(c)
