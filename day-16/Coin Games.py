n = int(input())
c = 0
j=1
while(n>=0):
    n-=j
    j+=1
    c+=1
print(c-1)
