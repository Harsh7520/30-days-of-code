n = int(input())
a = list(str(n))
if((a[0])=='-'):
    a.append('5')
elif(int(a[0])>=5):
    a.insert(1, '5')
else:
    a.insert(0, '5')
ans = ''.join(a)
print(int(ans))
