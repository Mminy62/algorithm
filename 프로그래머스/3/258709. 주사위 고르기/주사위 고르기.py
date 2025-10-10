'''
n개의 주사위 갖고 있음
주사위 6면은 각각 다른 번호가 써져있고, 1~n의 번호를 갖고 있다. 
주사위는 A, B가 절반씩 갖는다. A가 먼저 n/2개를 가져가고, 이후 B가 남은 것을 가져간다. 

가져간 n/2개 모두 굴린 뒤 나온 수들을 모두 합해 점수를 계산한다. 
점수가 큰 쪽이 승리, 점수가 같다면 무승부

n/2개에서
n/2개가 6번의 6 ** (n/2) 6 ** n/2 번끼리 
그럼 여기서 나온 합의 숫자들이 있을것. 

Counter로 

'''
import itertools
from collections import Counter

def solution(dice):
    answer = []
    n = len(dice)
    max_win = 0
    
    # 모든 조합 구하기
    comb_a_list = list(itertools.combinations(range(n), n//2))
    for comb_a in comb_a_list:
        comb_a = list(comb_a)
        comb_b = [i for i in range(n) if i not in comb_a]

        # a, b의 주사위 배열
        dice_a = [dice[a_idx] for a_idx in comb_a]
        dice_b = [dice[b_idx] for b_idx in comb_b]
        
        all_sums_a = [sum(x) for x in itertools.product(*dice_a)]
        all_sums_b = [sum(x) for x in itertools.product(*dice_b)]
        
        a_count = Counter(all_sums_a)
        b_count = Counter(all_sums_b)

        win_count = 0
        for a_val, a_freq in a_count.items():
            for b_val, b_freq in b_count.items():
                if a_val > b_val:
                    win_count += a_freq * b_freq
        
        if win_count > max_win:
            max_win = win_count
            answer = [x + 1 for x in comb_a]
    
    return answer