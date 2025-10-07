def solution(name, yearning, photo):
    answer = []
    memoryDic = dict(zip(name, yearning))
    
    for people in photo:
        score = 0
        for name in people:
            if name in memoryDic:
                score += memoryDic[name]
        answer.append(score)

    return answer