import re
def solution(s):
    answer = []
    s = s[1: -1]
    temp = []
    s = re.split("{|,{|},|}", s)
    for word in s:
        if not word:
            continue
        temp.append(list(map(int,word.split(","))))
    
    temp.sort(key=lambda x: len(x))

    for t in temp:
        for idx in range(len(t)):
            if t[idx] not in answer:
                answer.append(t[idx])
    

    return answer
