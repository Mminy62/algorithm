import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
for _ in range(n):
    info.append(int(input()))

info.sort()

s = info[0]
e = info[-1] * m #최대 시간 * 인원수
ans = e
while s <= e:
    mid = (s + e)//2
    total = 0

    for i in range(n):
        total += mid // info[i]

    if total < m:
        s = mid + 1
    else: # total >= m
        e = mid - 1
        ans = min(ans, mid)

print(ans)