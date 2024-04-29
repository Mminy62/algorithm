def solution(prices):
    answer = []
    n = len(prices)
    for i in range(1, n + 1):
        cur = prices[i - 1]
        ans = 0
        for j in range(i, n + 1):
            if prices[j - 1] < cur:
                ans = j - i
                break
        if not ans:
            ans = n - i
        
        answer.append(ans)
                
                
        
    
    return answer

'''
끝에서부터 기준으로, 최소값을 저장한 배열
'''

