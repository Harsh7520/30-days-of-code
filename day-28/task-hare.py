a = int(input())
b = int(input())
t = list(map(int,input().split()))
p = list(map(int,input().split()))
t.sort()
p.sort()
ans = 0
i = 0
j = 0
while i<a:
    while j<b:
        if(p[j]>=t[i]):
            ans+=1
            j+=1
            i+=1
        else:
            j+=1
    i+=1
print(ans)
