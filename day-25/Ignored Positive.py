n = int(input())
a = list(map(int, input().split()))
i = 1
while(True):
    if(i not in a):
        print(i)
        break
    else:
        i+=1
