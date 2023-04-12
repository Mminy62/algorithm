#완탐은 길이가 작으니까 전체 길이가 8인경우 -> 4만번 가능
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    dungeon_list = list(permutations(dungeons, n))
    
    for dungeon in dungeon_list:
        cnt = 0
        power = k
        for i in range(len(dungeon)): #dungeon: [80, 20], [50, 40], [30, 10]
            condition, cost = dungeon[i]
            if power <= 0:
                break
            if power >= condition:
                power -= cost
                cnt += 1    
        answer = max(answer, cnt)
        if answer == n:
            break
    
    return answer