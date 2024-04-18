import heapq
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    '''
    해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스 개발
    
    캐시에 없는 경우 5 -> 캐시에 넣기 
    # 가
    # 가장 오래된걸로 해가지구 heapq에 넣기 
    하나 빼서 
    '''
    n = len(cities)
    q = deque([])
    city_name = {}
    
    if not cacheSize:
        answer = len(cities) * 5
    else:
        for idx in range(n):
            city = cities[idx].lower()
            find_flag = False

            # 있는지 없는지 확인
            for j in range(len(q)):
                if city == q[j][1]:
                    q[j][0] = idx
                    find_flag = True
                    answer += 1

            if not find_flag: # 캐시에 없는 경우
                if len(q) == cacheSize: # 캐시 사이즈가 찬 경우
                    q = deque(sorted(q))
                    q.popleft()
                # 캐시 사이즈 안찬 경우
                q.append([idx, city])
                city_name[city] = idx
                answer += 5
                
    return answer