'''
하나의 키에 한번 눌렀을 때 나오는 문자가 있을 수도 있고, 
여러번 눌렀을때 나오는 문자가 있을 수 있음

keymap을 돌면서 가장 빠른 index를 갖는 것을 넣어야함 + 1
없으면 -1

'''
from collections import defaultdict
def solution(keymap, targets):
    answer = []
    dp = defaultdict(lambda: 101)
    # A - Z 까지의 알파벳을 기준으로 
    for c in range(ord('A'), ord('Z') + 1):
        for word in keymap:
            pos = word.find(chr(c))
            if pos >= 0 and pos < dp[chr(c)]:
                dp[chr(c)] = pos + 1  
    
    for word in targets:
        count = 0
        for c in word:
            if dp[c] == 101:
                count = -1
                break
            else:
                count += dp[c]
        answer.append(count)
        
    return answer