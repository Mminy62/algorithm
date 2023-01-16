from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    dict_term = {}
    for term in terms:
        k, v = term.split(" ")
        dict_term[k] = int(v)
        
    for i, p in enumerate(privacies):
        days = 0
        
        date, term = p.split(" ")
        yy, mm, dd = map(int,date.split("."))
        
        days += dict_term[term] * 28

        days += yy * 12 * 28
        days += mm * 28
        days += dd
        
        t = list(map(int,today.split(".")))
        t_num = t[0]*12*28 + t[1]*28 + t[2]
        if days <= t_num:
            answer.append(i+1)

    return answer