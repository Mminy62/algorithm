from collections import deque
n = int(input())
arr = deque(list(map(int, input().split())))
n += 1

def check_number():
    idx = 0
    while idx < n:
        if arr[n - 1 - idx] > 0:
            return idx
        idx += 1
    return -1


def check_last():
    if arr[-1] == 1 and sum(arr) == 1:
        return False
    return True

ans = 0 # = 연산자
while True:
    if arr[-1] != 0:
        if not check_last():
            print(ans)
            break

        ans += 1
        ans += len(str(arr[-1]))
        arr[-1] = 0
        # 나머지 뒤에서부터 확인해서 제일 처음 나오는 자리수 구하기


    else:
        # 뒤에 숫자가 0이고, 앞에 숫자가 하나라도 있다면, 그 index만큼 rotate 시키기
        idx = check_number()
        # idx만큼 rotate 시켜야해 그만큼 곱하고 2가 나왔으면
        ans += idx * 2
        arr.rotate(idx)