from functools import reduce
import math
n = int(input())
a = list(map(int,input().split()))
ans = reduce(math.gcd, a)
print(ans)
