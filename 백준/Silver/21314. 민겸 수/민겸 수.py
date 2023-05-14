from copy import deepcopy
minkyum = input()
max_result = ''
min_result = ''

def find_min(k_pos):
    result = ''
    temp = deepcopy(minkyum)
    pre = -1
    for k in k_pos:  # 완료된 인덱스 -> k까지
        n = k - pre - 1
        if n > 0:
            result += str(10 ** (n-1))
        pre = k
        result += '5'
    # if mmkmmm ->mmm 을 출력
    if pre != len(temp) - 1:
        cnt = len(temp[pre + 1:]) - 1
        result += str(10 ** cnt)

    return result

def find_max(k_pos):
    result = ''
    temp = deepcopy(minkyum)
    pre = -1
    for k in k_pos:  # 완료된 인덱스 -> k까지
        n = k - pre
        result += str(5 * (10 ** (n - 1)))
        pre = k
    # if mmkmmm ->mmm 을 출력
    if pre != len(temp)-1:
        cnt = len(temp[pre+1:])
        result += '1' * cnt
    return result


# k를 기준으로 나눠서 작성하지만, m만 있는 숫자인 경우
if 'K' not in minkyum:
    n = len(minkyum)
    max_result = '1' * n
    min_result = str(10 ** (n-1))


else:# k가 포함된 경우
    k_pos = []
    for i, v in enumerate(minkyum):
        if v == 'K':
            k_pos.append(i)
    max_result = find_max(k_pos)
    min_result = find_min(k_pos)

print(max_result)
print(min_result)