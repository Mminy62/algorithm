'''
n = 4 일 때,
마지막에 1칸을 뛸 경우 그 앞칸(n = 3)의 방법에서 +1만 하면 된다. 따라서 dp[i-1]
마지막에 2칸을 뛸 경우 그 앞앞칸(n = 2)의 방법에서 +2만 하면 된다. 따라서 dp[i-2]
'''
def solution(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        
    return dp[n]
# from math import comb
# def solution(n):#~2시까지
#     answer = 1
#     for i in range(1, n//2 + 1): # i 는 2의 개수
#         cnt2 = n - i * 2
#         numbers = i + cnt2
#         answer += comb(numbers, i)
    
#     return answer % 1234567