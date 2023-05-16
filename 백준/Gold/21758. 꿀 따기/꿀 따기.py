n = int(input())

data = list(map(int, input().split()))

# 벌통이 왼쪽에 있는 경우 -> 처음 벌은 가장 오른쪽
# 두번째 벌은 가장 끝을 제외한 나머지에서 누적합이 큰 곳으로
left_dp = [data[0]]

for i in range(1, n):
    left_dp.append(sum(data[:i + 1]))

# 1. 벌통이 왼쪽에 있는 경우, 첫 벌은 가장 오른쪽
# 두번째 벌은 가장 끝을 제외한 나머지에서 누적합이 큰 곳으로
lans = 0

for i in range(1, n-1):
    lans = max(lans, left_dp[n-2] + left_dp[i-1] - data[i])

# 2. 벌통이 가장 오른쪽에 있는 경우, 첫 벌은 가장 왼쪽에 있다.
rans = 0
right_dp = []
for i in range(n-1, -1, -1):
    right_dp.append(sum(data[i:n]))

right_dp.reverse()

for i in range(n-2, 0, -1):
    rans = max(rans, right_dp[1] + right_dp[i+1] - data[i])

#3. 벌이 양쪽에 있고 가운데에 통이 있는 경우
cans = 0
for i in range(1, n-1):
    cans = max(cans, left_dp[n-2] - data[0] + data[i])

print(max(lans, cans, rans))