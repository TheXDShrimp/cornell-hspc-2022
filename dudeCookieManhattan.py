import math

# Read input
xc, yc, r = map(int, input().split())
xd, yd = map(int, input().split())

# Calculate distance to closest point on cookie circumference
if xd <= xc - r:
    xp = xc - r
    if yd <= yc - r:
        yp = yc - r
        distance = abs(xp - xd) + abs(yp - yd)
    elif yd >= yc + r:
        yp = yc + r
        distance = abs(xp - xd) + abs(yp - yd)
    else:
        distance1 = abs(xp - xd) + abs(yc - r - yd)
        distance2 = abs(xp - xd) + abs(yc + r - yd)
        distance = min(distance1, distance2)
elif xd >= xc + r:
    xp = xc + r
    if yd <= yc - r:
        yp = yc - r
        distance = abs(xp - xd) + abs(yp - yd)
    elif yd >= yc + r:
        yp = yc + r
        distance = abs(xp - xd) + abs(yp - yd)
    else:
        distance1 = abs(xp - xd) + abs(yc - r - yd)
        distance2 = abs(xp - xd) + abs(yc + r - yd)
        distance = min(distance1, distance2)
else:
    if yd <= yc - r:
        yp = yc - r
        distance = abs(xc - r - xd) + abs(yp - yd)
    elif yd >= yc + r:
        yp = yc + r
        distance = abs(xc - r - xd) + abs(yp - yd)
    else:
        distance1 = abs(xc - r - xd) + abs(yc - r - yd)
        distance2 = abs(xc + r - xd) + abs(yc - r - yd)
        distance3 = abs(xc - r - xd) + abs(yc + r - yd)
        distance4 = abs(xc + r - xd) + abs(yc + r - yd)
        distance = min(distance1, distance2, distance3, distance4)

# Print answer
print(distance)
