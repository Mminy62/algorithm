'''
n미터
1미터씩 나눴으면 그 안에서만 롤러가 움직여야함
벽에서 롤러를 떼면 그게 1번
m, n 
1, 2, 3, 4, 5

오름차순 section
어차피 2 + 4까진 칠하기 가능 2+4 - 1=5 그럼 5에 해당하는건 삭제 2, 3 삭제 
6 + 4

1 + 1 - 1 = 1 1까지 해당하는 것 삭제



'''
from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    
    while (section):
        answer += 1
        start = section.popleft()
        end = start + m
        
        while (section and section[0] < end):
            section.popleft()
    
    return answer