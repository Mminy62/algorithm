from collections import defaultdict
from itertools import product

def solution(user_id, banned_id):
    answer = 0
    banned_list = defaultdict(set)
    n = len(banned_id)
    for bid in banned_id:
        for uid in user_id:
            correct = True
            if len(uid) == len(bid):
                for a, b in zip(uid, bid):
                    if b == "*":
                        continue
                    if a != b:
                        correct = False
                if correct:# 필러팅에 걸리는 아이디
                    banned_list[bid].add(uid)
    
    temp = []
    for key in banned_id:
        temp.append(list(banned_list[key]))
        
    result = set()
    for name_list in product(*temp):
        if len(set(name_list)) == n:
            result.add(tuple(sorted(name_list)))

    return len(result)

'''
각 banned id 에 대한 가능한 경우의 수를 넣고
하나씩 뽑은 comb를 만든다. 
 -> comb에 대한 set이 len 으로 해서 len(banned_id) 와 같으면 경우의 수로 인정
'''