n = int(input())
a = int(input())
b = int(input())
without_front = n-a
if(without_front<=b):
    print(without_front)
else:
    print(without_front - (without_front-b) + 1)
