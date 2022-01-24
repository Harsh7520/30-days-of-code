def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
n = int(input())
num = 29
lst = []
for _ in range(99999):
  s = sum_digits(num)
  if(s==11):
      lst.append(num)
  num = num+1
print(lst[n-1])
