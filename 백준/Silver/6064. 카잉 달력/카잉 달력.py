import math
n = int(input())
for _ in range(n):
    M, N, x, y = map(int, input().split())
    range_num = M * N // math.gcd(M, N) # lcm

    max_k = (range_num - x) // M
    coords = []
    for k in range(max_k + 1):
        coords.append(M * k + x)

    result = -1
    for num in coords:
        if (num - y) % N == 0:
            result = num
            break

    print(result)