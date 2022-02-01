n = int(input())
k = int(input())
a = list(map(int, input().split()))
last = dict()
time = 0
for task in a:
    if task not in last:
        pass
    elif time - last[task] < k:
        time = k + last[task]
    time += 1
    last[task] = time
print(time)
