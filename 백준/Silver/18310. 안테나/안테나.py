n = int(input())

house = list(map(int, input().split()))
house.sort()

if n % 2 == 0:
    avg = (house[(n//2)-1] + house[n//2]) / 2
    be = abs(avg - house[n//2-1])
    af = abs(avg - house[n//2])
    if be <= af:
        med = house[n//2-1]
    else:
        med = house[n//2]
else:
    med = house[n//2]

print(med)