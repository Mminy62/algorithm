import re
def solution(s):
    answer = []
    temps = s.lstrip("{").rstrip("}").split("},{")
    
    new = []
    for word in temps:
        new.append(list(map(int, word.split(","))))
    
    new.sort(key=len)
    
    for words in new:
        for word in words:
            if word not in answer:
                answer.append(word)
        
    return answer
