n = int(input())
a = list(map(int,input().split()))
max_1 = max(a)
a.remove(max_1)
max_2 = max(a)
min_1 = min(a)
a.remove(min_1)
min_2 = min(a)

if((min_1*min_2)>(max_1*max_2)):
    print(min_1*min_2)
else:
    print(max_1*max_2)
