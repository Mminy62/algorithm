import re
def solution(s):
    answer = []
    
    for i, c in enumerate(s):
        if c in s[:i]:
            answer.append(s[:i:][::-1].find(c)+1)
        else:
            answer.append(-1)
    return answer