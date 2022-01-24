import math
def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)
n = int(input())
b = False
for i in range(int(math.sqrt(n)) + 5):
    if fact(i) == n:
        b = True
        print(i)
        break
if b:
    pass
else:
    print(-1)
