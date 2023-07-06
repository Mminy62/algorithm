import sys
input = sys.stdin.readline

N, C = map(int, input().split())

m = int(input())
infos = []
for _ in range(m):
    s, r, box = map(int, input().split())
    infos.append((s, r, box))

capa = [C] * (N+1)
# s~r의 범위에서 capa, box 합쳐서 작은 값을 찾아,
# 해당 값을 다 더하는 것

total = 0
infos.sort(key=lambda x: x[1])

for s, r, box in infos:
    min_value = C

    for i in range(s, r):
        if min_value > min(capa[i], box):
            min_value = min(capa[i], box)

    for i in range(s, r):
        capa[i] -= min_value

    total += min_value

print(total)