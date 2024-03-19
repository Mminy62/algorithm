N, K = map(int, input().split())
array = [0]
for _ in range(N):
    array.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]

# 무게에 대해 물건이 포함 되는지 안되는지 확인
for i in range(1, N + 1):
    w, v = array[i]

    for kg in range(K + 1):
        if kg - w >= 0:
            dp[i][kg] = max(dp[i-1][kg], dp[i-1][kg-w] + v)
        else:
            dp[i][kg] = dp[i-1][kg]

print(dp[-1][-1])