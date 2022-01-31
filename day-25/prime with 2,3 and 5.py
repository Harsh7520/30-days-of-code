import math
def primefactors(n):
    while n % 2 == 0:
        a.append(2),
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            a.append(i)
            n = n / i
    if n > 2:
        a.append(n)
n = int(input())
a = []
b = True
primefactors(n)
for i in a:
    if(i>5):
        b = False
if(b):
    print("true")
else:
    print("false")
