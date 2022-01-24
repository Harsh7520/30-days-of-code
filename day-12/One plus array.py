n = int(input())
a = list(map(int,input().split()))
strings = [str(i) for i in a]
a_string = "". join(strings)
an_integer = int(a_string)
an_integer += 1
ans = list(str(an_integer))
print(*ans)
