def solution(sticker):
    answer = 0
    if len(sticker) < 3:
        return max(sticker)
    
    n = len(sticker)
    
    dp1 = [0] * n
    
    # 1번을 떼는 경우
    dp1[0], dp1[1] = sticker[0], sticker[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # 2번을 떼는 경우
    dp2 = [0] * n
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i - 2] + sticker[i])
    
    
    return max(max(dp1), max(dp2))