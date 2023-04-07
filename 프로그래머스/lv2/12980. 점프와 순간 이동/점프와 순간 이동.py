def solution(n):
    ans = 0
# dp = [0] * (n + 1)
    #초기화
#     for i in range(n + 1):
#         dp[i] = i

#     for i in range(2, n + 1):
#         if i % 2 == 0:
#             dp[i] = min(dp[i], dp[i//2], dp[i-1] + 1)
#         else:
#             dp[i] = min(dp[i], dp[i-1] + 1)
# O(N) -> 시간 초과
            
    while(n > 0):
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
        

    return ans