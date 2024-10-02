from collections import Counter

def solution(participant, completion):
    answer = ''
    set_part = set(participant)
    set_com = set(completion)
    
    result = set_part - set_com
    if result:
        answer = result.pop()
    
    else: # 동명이인이 답인 경우
        count_part = Counter(participant)
        count_com = Counter(completion)
        for part, com in zip(sorted(count_part.items()), sorted(count_com.items())):
            if part[1] != com[1]:
                answer = part[0]
    
    return answer