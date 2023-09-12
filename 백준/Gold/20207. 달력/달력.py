n = int(input())
calendar = []
height = [0] * 366

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        height[i] += 1
    calendar.append([a, b])

calendar.sort()
result = 0
s, e = calendar[0]

for a, b in calendar[1:]:
    if e+1 < a:
        result += (e-s + 1) * max(height[s:e+1])
        height[e] = 0
        s = a

    if b > e:
        e = max(b, e)

if height[e]:
    result += (e-s + 1) * max(height[s:e+1])

print(result)