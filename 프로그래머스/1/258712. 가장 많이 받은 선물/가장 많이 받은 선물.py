'''
이번 달을 기반으로 다음 달 받은 선물 수를 예측

두사람사이에 비교
1. A, B 가 이번달 주고 받은 선물 기록으로 비교
2. 없거나 같다면 선물 지수로 비교
    - 선물지수: 이번 달 친구들에게 준 선물 수 - 받은 선물 수
3. 선물 지수도 같다면, 다음 달 선물을 주고 받지 않는다

다음달 가장 많이 받은 사람의 선물의 수

A -> B

friends끼리 전부 비교 - 50 * 50

1. 이름별 인덱스를 가진 dict
2. 이중배열 생성(선물 주고 받은 배열)
3. 선물지수를 담은 dict 생성
4. friends 이중 포문으로 다음달 예측

'''
from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    name_dic = dict()
    n = len(friends)
    
    for idx, name in enumerate(friends):
        name_dic[name] = idx
    
    gift_arr = [[0] * n for _ in range(n)]
    
    # 선물 기록으로 gift_arr
    for record in gifts:
        A, B = record.split()
        gift_arr[name_dic[A]][name_dic[B]] += 1
    
    # 선물 지수
    gift_dic = dict()
    for i, name in enumerate(friends):
        gift_dic[name] = sum(gift_arr[i]) - sum([gift_arr[row][i] for row in range(n)])
    
    next_gift = defaultdict(lambda: 0)
    for name1 in friends:
        for name2 in friends:
            if name1 == name2:
                continue
            name1_cnt = gift_arr[name_dic[name1]][name_dic[name2]]
            name2_cnt = gift_arr[name_dic[name2]][name_dic[name1]]
            if name1_cnt > name2_cnt:
                next_gift[name1] += 1
            elif name1_cnt < name2_cnt:
                next_gift[name2] += 1
            else:
                # 선물 지수
                if gift_dic[name1] > gift_dic[name2]:
                    next_gift[name1] += 1
                elif gift_dic[name1] < gift_dic[name2]:
                    next_gift[name2] += 1
    
    return max(next_gift.values()) // 2 if next_gift else 0