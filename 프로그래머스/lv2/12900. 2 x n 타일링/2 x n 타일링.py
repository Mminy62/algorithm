def solution(n):
    answer = 0
    '''
    DP, 점화식 문제
    '''
    dp = [0 for i in range(n)]
    
    dp[0], dp[1] = 1, 2
    
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n-1]