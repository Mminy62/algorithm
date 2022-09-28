from itertools import combinations
from functools import reduce 
import operator
import math


def solution(clothes):
    answer = 0
    
    clothDict = {}
    
    #key별로 clothes 수 values에 넣기
    for v, k in clothes:
        count = 1
        if k not in clothDict.keys():
            clothDict[k] = count
        else:
            clothDict[k] = clothDict[k]+1
    
    clothType = len(clothDict.keys())
    result = ""
    
    temp = list(clothDict.values())
    for i in range(len(temp)):
        result += "({0}+1)*".format(temp[i])
        
    answer = eval(result[:-1])-1
    

    # for i in range(1, clothType + 1):
    #     if i == 1:
    #         answer += sum(clothDict.values())
    #     else:
    #         temp = list(combinations(clothDict.values(),i)) #key들로 comb만들기
    #         print(temp)
    #         for data in temp:
    #             answer += reduce(operator.mul, data, 1)
            
    return answer