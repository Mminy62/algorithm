def solution(n, lost, reserve):
    answer = n - len(lost)
    
    count = 0
    lost.sort()
    reserve.sort()
    
    intersection = list(set(lost) & set(reserve))
    if intersection:
        answer += len(intersection)
        reserve = list(set(reserve) - set(intersection))
        for data in intersection:
            lost.remove(data)
        
    for item in lost:
        # if item in reserve:
        #     reserve.remove(item)
        #     count += 1
        
        if item - 1 in reserve:
            reserve.remove(item - 1)
            count += 1
            print(item-1, count)
            
        elif item + 1 in reserve:
            reserve.remove(item + 1)
            count += 1
            print(item+1, count)
        
        elif reserve == []:
            break
            

    answer += count
    
    return answer