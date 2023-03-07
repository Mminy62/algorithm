def solution(n):
    answer = 0
    dp = [0] * 50001
    
    dp[1] = 0
    dp[2] = 3
    # f(n) 계산 전에 f(n-2)까지의 dp를 완성시켜야 한다. 
    for i in range(4, n + 1, 2):
        dp[i] = (3 * dp[i-2] + 2 * sum(dp[:i-3]) + 2) % 1000000007

    return dp[n]