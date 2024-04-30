import heapq
from collections import deque
def solution(begin, target, words):
    answer = 0
    
    # 변환할 수 없는 경우
    if target not in words:
        return 0
    
    n = len(begin)
    q = deque([])
    print(list(enumerate(target)))
    # 처음 q초기화 - words에서 한글자 바뀐 후보 찾기
    for word in words:
        origin = set(begin)
        if len(set(list(enumerate(begin))) | set(list(enumerate(word)))) == n + 1: # 한글자 차이인 word
            q.append((word, 1))
    
    while q:
        item, cnt = q.popleft()
        print(item)
        if item == target:
            return cnt
        
        for word in words:
            if len(set(list(enumerate(item))) | set(list(enumerate(word)))) == n + 1:
                q.append((word, cnt + 1))
    
    return answer