d = [0] * 1000001

n = int(input())

for i in range(2, n+1):
    #1뺀 것에 대해서
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])