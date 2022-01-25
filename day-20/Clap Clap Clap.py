n = int(input())
a = []
for i in range(1,n+1):
    if(i%3==0):
        a.append("clap")
    elif("3" in str(i)):
        a.append("clap")
    elif ("6" in str(i)):
        a.append("clap")
    elif ("9" in str(i)):
        a.append("clap")
    else:
        a.append(i)
print(*a)
