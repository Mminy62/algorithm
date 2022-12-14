n = int(input())
info = []

for _ in range(n):
    info.append(input().split())

info.sort(key = lambda x: int(x[0]))

for item in info:
    print(item[0], item[1])