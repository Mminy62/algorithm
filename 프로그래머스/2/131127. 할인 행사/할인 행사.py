'''
일정 금액을 지불하면 10일동안 회원 자격 부여
할인 제품은 각 날마다 달라, 하루에 하나씩만 구매 가능

원하는 제품/수량이 
할인하는 날짜와 10일 연속응로 일치하는 경우 -> 회원가입
'''
from copy import deepcopy

def solution(want, number, discount):
    answer = 0
    info = {}
    for key, value in zip(want, number):
        info[key] = value

    # info 를 카피한 걸 value의 합이 다 0이면 ok
    n = len(discount)
    for start in range(n - 10 + 1):
        cnt = 10
        temp_info = deepcopy(info)
        
        for i in range(start, start + 10):
            item = discount[i]
            if item in want and temp_info[item] > 0:
                temp_info[item] -= 1
                cnt -= 1
            else:
                break
                
        if cnt == 0:
            answer += 1

    return answer