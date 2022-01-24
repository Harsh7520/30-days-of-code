import math
n = input()
lst = list(map(int,n))
sum = 0
for i in lst:
    sum = sum + math.factorial(i)
if(sum==int(n)):
    print("Yes")
else:
    print("No")
