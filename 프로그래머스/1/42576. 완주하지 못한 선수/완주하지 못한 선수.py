from collections import Counter

def solution(participant, completion):
    count_part = Counter(participant)
    count_com = Counter(completion)
    answer = count_part - count_com
    
    return list(answer.keys())[0]