def minStartValue(nums):
    minValue = 0
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        minValue = min(minValue, sum)
    startValue = 1 - minValue
    return startValue
n = int(input())
a = list(map(int,input().split()))
print(minStartValue(a))
