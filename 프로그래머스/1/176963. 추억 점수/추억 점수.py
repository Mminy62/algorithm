def solution(name, yearning, photo):
    answer = []
    memoryDic = dict()
    for (name, score) in zip(name, yearning):
        memoryDic[name] = score
    
    for people in photo:
        memoryScore = 0
        for name in people:
            if name in memoryDic.keys():
                memoryScore += memoryDic[name]
        answer.append(memoryScore)

    return answer