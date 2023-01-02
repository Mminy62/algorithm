def solution(s):
    s = list(s.lower())
    
    pcnt = len(list(filter(lambda x : x == "p", s)))
    ycnt = len(list(filter(lambda x : x == "y", s)))
    
    if pcnt == ycnt:
        return True
    else:
        return False