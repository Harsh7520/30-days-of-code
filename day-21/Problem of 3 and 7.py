n = int(input())
b = False
for i in range(0,n+1,7):
         if (n-i)%3 == 0:
            b = True
            break
         else:
            b = False
if(b):
    print("true")
else:
    print("false")
