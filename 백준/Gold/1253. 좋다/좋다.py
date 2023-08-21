from bisect import bisect_right
import sys
input = sys.stdin.readline

n = int(input())

target = 0
array = list(map(int, input().split()))
array.sort()
cnt = 0

if n > 2:
    for i in range(n):
        tmp = array[:i] + array[i + 1:]
        target = array[i]
        start = 0
        end = len(tmp)-1

        while start < end:
            t = tmp[start] + tmp[end]

            if t == target:
                cnt += 1
                break
            elif t > target:
                end -= 1
            else:
                start += 1


print(cnt)