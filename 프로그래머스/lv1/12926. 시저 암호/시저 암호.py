def solution(s, n):
    answer = []
    
    for c in list(s):
        if c.isalpha():
            temp = ord(c) + n
    
            if c.islower() and temp > 122 or c.isupper() and temp > 90:
                temp -= 26
            
            answer.append(chr(temp))
        else:
            answer.append(c)
                
    return ''.join(answer)