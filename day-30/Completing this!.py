n = int(input())
a = list(map(int, input().split()))
odd = a[::2]
even = a[1::2]
sum_odd = sum(odd)
sum_even = sum(even)
print(max(sum_odd, sum_even))
