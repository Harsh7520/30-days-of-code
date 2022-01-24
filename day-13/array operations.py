n = int(input())
a = list(map(str, input().split()))
m = int(input())
s1 = "".join(a)
i_s1 = int(s1)
ans = i_s1 + m
f_ans = list(str(ans))
print(*f_ans)
