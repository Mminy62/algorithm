n, m = map(int, input().split())
array = [[0] * (m + 1)]
for _ in range(n):
    temp = [0] + list(map(int, input().split()))
    array.append(temp)

command = int(input())

for _ in range(command):
    result = 0
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sx, ex + 1):
        for j in range(sy, ey + 1):
            result += array[i][j]

    print(result)