import math


def Log2(x):
    if x == 0:
        return False

    return (math.log10(x) /
            math.log10(2))


def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))
n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    for j in range(len(a)):
        if(i<j):
            if(isPowerOfTwo(a[i]+a[j])):
                count+= 1
print(count)
