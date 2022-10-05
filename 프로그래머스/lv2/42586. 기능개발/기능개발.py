def solution(progresses, speeds):
    answer = []

    state = []
    t = 8
    
    while speeds:#남아있을때 까지
        #시간이 지날때마다 더하는 것 
        if state == []:
            state = list(map(lambda x: x[0] + x[1], list(zip(progresses, speeds))))
        else:
            state = list(map(lambda x: x[0] + x[1], list(zip(state, speeds))))
        
        
        if state[0] >= 100:
            result = [0 if v >= 100 else 1 for v in state] 
            count = 0
            
            for data in result:
                if data == 0:
                    count += 1
                    state.pop(0)
                    speeds.pop(0)
                else:
                    break
                    
            if count != 0:
                answer.append(count)
                
            
    return answer

'''
    맨 위가 100이상일 때 pop 시키는데 
    그 뒤에도 100이상인게 있으면 같이 pop 시키고, 한번에 pop시키는 갯수를 세서 answer에 추가. 
    
    '''