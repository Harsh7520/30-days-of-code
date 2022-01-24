n = int(input())
str_n = str(n)
sqr = n*n
str_sqr = str(sqr)
rev = str_sqr[::-1]
if(rev.startswith(str_n[::-1])):
    print("Phoenix number")
else:
    print("Not a phoenix number.")
