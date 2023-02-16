n = int(input())
cnt = 0

soldiers = list(map(int, input().split()))
soldiers.reverse()
dp = [1] * n #부분 수열의 명 수 표시 #해당 인덱스까지의 연속된 숫자

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))