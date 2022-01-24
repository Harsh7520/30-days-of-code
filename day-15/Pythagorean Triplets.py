n = int(input())
a = list(map(int,input().split()))
b = False
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            if((a[i])**2 + (a[j])**2 == (a[k])**2):
                b = True

                break

if(b==False):
    print("false")
else:
    print("true")
