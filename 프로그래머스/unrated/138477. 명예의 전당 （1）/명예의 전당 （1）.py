def solution(k, score):
    answer = []
    honor = []
    
    for i, v in enumerate(score):
        if k >= len(score):
            honor.append(v)
            honor.sort()
            
        else:
            if len(honor) < k:
                honor.append(v)
                honor.sort()
            else:
                if v > honor[0]:
                    honor[0] = v
                    honor.sort()
            
        answer.append(honor[0])     
    
    return answer