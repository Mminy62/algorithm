from itertools import combinations

def solution(brown, yellow):#2:30-3:00
    # br + ye 의 약수로 comb
    n = brown + yellow
    nums = []
    for x in range(3, n - 2):
        if n % x == 0 and x >= n // x and n // x > 2:
            y = n // x
            nums.append((x, y))
    
    # 가운데에 yellow 가 들어가는지 확인
    for x, y in nums:
        if (x - 2) * (y - 2) == yellow:
            return [x, y]
