import math

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    # 집합 만들기
    one_set = []
    two_set = []
    sim = 0
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            one_set.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            two_set.append(str2[i] + str2[i + 1])

    if not one_set and not two_set:
        sim = 1 # 유사도
    else:
        # 다중집합의 합집합 & 교집합인 것
        # 다중집합의 합집합
        temp = one_set.copy()
        union = one_set.copy()
        for i in two_set:
            if i not in temp:
                union.append(i)
            else:
                temp.remove(i)
        # 다중집합의 교집합
        temp = one_set.copy()
        inter = []
        for i in two_set:
            if i in temp:
                inter.append(i)
                temp.remove(i)

        sim = len(inter) / len(union)

    # 유사도 구하기
    answer = math.floor(sim * 65536)


    return answer