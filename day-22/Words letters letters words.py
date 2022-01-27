def Convert(string):
    a=[]
    a[:0]=string
    return a

s1 = input()
n = int(input())
s2 = input()
a = Convert(s1)
b = s2.split(" ")
lst = []
for item in b:
    ls = Convert(item)
    ls.sort()
    lst.append(ls)
a.sort()
max_count = 0
for word in b:
    if all(a.count(c) >= word.count(c) for c in word):
        if(max_count<len(word)):
            max_count = len(word)
print(max_count)
