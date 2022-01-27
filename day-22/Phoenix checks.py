def Convert(string):
    a=[]
    a[:0]=string
    return a
s1 = input()
s2 = input()
a = Convert(s1)
b = Convert(s2)
a.sort()
b.sort()
if(a==b):
    print("true")
else:
    print("false")
