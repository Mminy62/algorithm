def solution(survey, choices):
    answer = ''
    
    score_dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0 }
    
    for k, v in zip(survey, choices): #문제 수 
        a, b = list(k)
        if v < 4: 
            score_dict[a] += abs(4-v)
        else:
            score_dict[b] += abs(4-v)
    
    indic = [["R", "T"], ["C","F"], ["J", "M"], ["A", "N"]]
    for i in range(len(indic)):
        f, s = indic[i]
        answer+=((f if score_dict[f] >= score_dict[s] else s))
    
    return answer