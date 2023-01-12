def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    if len(score) < m:
        return 0
    else:
        for i in range(m-1, len(score) ,m):
            answer += (score[i] * m)
            
        return answer