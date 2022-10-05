def solution(answers):
    answer = []
    result = []
    
    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    testNum = len(answers)
    
    multiple = []
    for i in range(3):
        multiple = testNum//len(p[i])
        
        if testNum%len(p[i]) != 0:
            multiple += 1

        p[i] = p[i] * (multiple)
        
    
    for i in range(len(p)):
        temp = list(map(lambda x, y: 1 if x == y else 0, answers, p[i][0:len(answers)]))
        result.append(sum(temp))
        
    
    return [i+1 for i, v in enumerate(result) if v == max(result)]
    