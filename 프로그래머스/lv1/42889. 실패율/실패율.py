def solution(N, stages):
    result = {}
    total = len(stages)
    
    for i in range(1, N+1):
        if total != 0:
            result[i] = (stages.count(i)/total)
            total -= stages.count(i)
        else:
            result[i] = 0
    
    return sorted(result, key=lambda x : result[x], reverse=True)
    # result = sorted(result.items(), key = lambda item : item[1], reverse = True)
    # return list(dict(result).keys())