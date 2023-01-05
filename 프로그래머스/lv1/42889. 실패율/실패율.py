def solution(N, stages):
    result = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if total == 0:
            result[i] = 0
        elif i in stages:
            result[i] = (stages.count(i)/total)
            total -= stages.count(i)
        else:
            result[i] = 0
    
    result = sorted(result.items(), key = lambda item : item[1], reverse = True)
    
    
    return list(dict(result).keys())