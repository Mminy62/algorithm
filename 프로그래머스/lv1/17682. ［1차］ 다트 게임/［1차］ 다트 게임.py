def solution(dartResult):
    result = []

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1}

    dlist = list(dartResult)
    
    for i, v in enumerate(dlist):
        temp = 0
        
        if v.isdecimal():
            #score
            if dlist[i-1].isdecimal():
                continue
            if dlist[i+1].isdecimal():
                score = int(v + dlist[i+1])
                i += 1

            else:
                score = int(v)
            #bonus
            temp = score ** (bonus[dlist[i+1]])
            
            #option
            if (i+2) < len(dartResult) and not dlist[i+2].isdecimal():
                #마지막 안넘게
                if dlist[i+2] == '*' and result:
                    
                    result[-1] *= 2
                    temp *= 2
                    
                elif dlist[i+2] == '#' and result:
                    temp *= -1
                elif not result:#result빈 첫 항
                    temp = temp * option[dlist[i+2]]
                    
            result.append(temp)  
    
    return sum(result)