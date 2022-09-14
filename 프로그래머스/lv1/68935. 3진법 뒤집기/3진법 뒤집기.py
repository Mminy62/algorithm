import string

tmp = string.digits+string.ascii_lowercase

def convert(n, base):
    
    q, r = divmod(n, base)
    
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base) + tmp[r]
    
def nTo10(n):
    
    n = str(n)[::-1]
    result = 0
    
    for i in range(len(n)):
        result += int(n[i]) * (3 ** i)
        
    return result
    
    
def solution(n):
    answer = 0
    
    temp = str(convert(n,3))[::-1]

    answer = nTo10(int(temp))
    
    
    return answer