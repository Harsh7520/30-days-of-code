hour = int(input())
minute = int(input())
if (hour == 12):
    hour = 0
if (minute == 60):
    minute = 0
    hour += 1
    if (hour > 12):
        hour = hour - 12
hour_in_min = hour*60/2 + minute/2
min_angle = 6*minute
angle = abs(hour_in_min-min_angle)
angle = min(360-angle,angle)
print(int(angle))
