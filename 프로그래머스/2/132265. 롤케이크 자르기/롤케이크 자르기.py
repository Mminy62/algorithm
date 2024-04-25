def solution(topping):
    answer = 0
    count = dict() # 그냥 dict로도 되는구나
    for i in topping:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    leftdata = dict()
    for i in topping:
        if i not in leftdata:
            leftdata[i] = 1
        else:
            leftdata[i] += 1
            
        if count[i] == 1:
            del count[i]
        else:
            count[i] -= 1
            
        
        if len(leftdata.keys()) == len(count.keys()):
            answer += 1
            
    return answer
