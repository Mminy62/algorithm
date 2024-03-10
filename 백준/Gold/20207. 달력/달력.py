n = int(input())
dates = []
for _ in range(n):
    dates.append(tuple(map(int, input().split())))

dates.sort(key=lambda x: (x[0], -(x[1]-x[0])))

result = 0
width = 0
start, end = 0, 0
#시작-끝에 높이 배열을 준다
heights = [0] * 366

for s2, e2 in dates:
    for i in range(s2, e2 + 1):
        heights[i] += 1

    if start == 0:
        start = s2
        end = e2
        continue

    if end + 1 < s2:
        width = (end + 1) - start
        height = max(heights[start: end + 1])
        result += width * max(heights[start: end + 1])
        start = s2

    if e2 > end:
        end = e2

# 마지막 값
width = (end + 1) - start
height = max(heights[start: end + 1])
result += width * max(heights[start: end + 1])

print(result)