import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))
length = n

if sum(array) < s:
    length = 0
else:
    lp, rp = 0, 0
    temp = array[lp]
    while True:
        if temp < s:
            rp += 1
            if rp == n: break
            temp += array[rp]
        else:
            length = min(length, rp-lp + 1)
            temp -= array[lp]
            lp += 1
print(length)