import sys
input = sys.stdin.readline

n = int(input())

points = [tuple(map(int,input().split())) for _ in range(n)]
lines = []

for s, e in points:
    lines.append((s, 1))
    lines.append((e, -1))

lines.sort(key=lambda x: (x[0], x[1]))

cnt = 0
ans = 0
for s, v in lines:
    cnt += v
    ans = max(ans, cnt)

print(ans)