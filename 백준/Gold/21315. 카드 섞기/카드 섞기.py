import math
from copy import deepcopy
from itertools import product

n = int(input())
result = list(map(int, input().split()))
origin = [i for i in range(1, n+1)]
max_k = int(math.log2(n))
candi = list(product(range(1, max_k + 1), range(1, max_k + 1)))


for data in candi:
    cards = deepcopy(origin)
    for k in data:
        tmp = []
        for i in range(1, k + 2):
            # 첫번째 단계
            if i == 1:
                tmp = cards[-2**k:]
                del cards[-2**k:]
                cards = tmp + cards
            else: #나머지 단계
                tmp = tmp[-2**(k-i+1):]
                cards = list(filter(lambda x: x not in tmp, cards))
                cards = tmp + cards
    if cards == result:
        print(' '.join(map(str,data)))
        break


