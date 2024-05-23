from itertools import combinations_with_replacement, permutations
from collections import defaultdict
import heapq
import sys

def solution(k, n, reqs):
    answer = sys.maxsize
    temp_combinations = combinations_with_replacement(range(1, n + 1), k) #max: 42000
    valid_combinations = [comb for comb in temp_combinations if sum(comb) == n]
    # 각 조건에 대한 순열
    
    mentors = defaultdict(list)
    wait_time = []
    
    for temp_comb in valid_combinations:
        for comb in list(set(permutations(temp_comb))):
            # comb에 따라 상담사 유형에 인원 배치, 초기화
            mentors = defaultdict(list)
            temp_wait = 0
            for i in range(1, k + 1):
                for _ in range(comb[i - 1]):
                    heapq.heappush(mentors[i], 0)

            for start, time, key in reqs:
                end = heapq.heappop(mentors[key])
                if end > start:
                    temp_wait += end - start
                    heapq.heappush(mentors[key], end + time)
                else:# end <= start
                    heapq.heappush(mentors[key], start + time)
            
            answer = min(answer, temp_wait)
 
    return answer
