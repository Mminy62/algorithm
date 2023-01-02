def solution(s):
    return s.lower().count('p') == s.lower().count('y')
#     s = list(s.lower())
    
#     pcnt = len(list(filter(lambda x : x == "p", s)))
#     ycnt = len(list(filter(lambda x : x == "y", s)))
    
#     if pcnt == ycnt:
#         return True
#     else:
#         return False