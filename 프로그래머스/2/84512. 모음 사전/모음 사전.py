from itertools import product
from bisect import bisect_left
def solution(word):
    answer = 0
    info = []
    temp = ['A', 'E', 'I', 'O', 'U']
    num = 0
    for re in range(1, 6):
        array = list(product(temp, repeat=re))
        for item in array:
            info.append(''.join(item))
    
    info.sort()  
    
    return bisect_left(info, word) + 1