from functools import reduce
def solution(s):
    answer = ''
    #ord -> sort -> chr -> connect
    
    s = list(map(lambda x : ord(x), list(s)))
    
    s.sort(reverse=True)
    
    answer = list(map(lambda x : chr(x), s))
        
    return reduce(lambda x, y: x + y, answer)