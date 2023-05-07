from copy import deepcopy
n, k = map(int, input().split())

s = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

p = [0] * (n + 1)

for _ in range(k):
    for i in range(1, n + 1):
        p[d[i]] = s[i]
    s = deepcopy(p)

print(*p[1:])