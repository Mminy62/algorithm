from sys import maxsize
res = [maxsize, -maxsize]

def count_odds(x):
    cnt = 0
    array = list(x)
    odd = '13579'
    for data in array:
        if data in odd:
            cnt += 1
    return cnt


def cal(num, odd_cnt):
    if len(num) == 1:
        res[0] = min(res[0], odd_cnt + count_odds(num))
        res[1] = max(res[1], odd_cnt + count_odds(num))
        return

    elif len(num) == 2:
        cal(str(int(num[:1]) + int(num[1:])), odd_cnt + count_odds(num))
    else:#len(num) >= 3
        for i in range(1, len(num)-1):
            for j in range(i + 1, len(num)):
                cal(str(int(num[:i]) + int(num[i:j]) + int(num[j:])), odd_cnt + count_odds(num))

n = input()
cal(n, 0)


print(*res, sep=' ')