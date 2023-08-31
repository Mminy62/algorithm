import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

left, right = 0, 0
cnt = 1 if array[left] % 2 != 0 else 0
result = 0
while left < n and right < n:
    if left > right:
        break

    if cnt <= k:
        result = max(result, right - left + 1 - cnt)
        right += 1
        if right < n and array[right] % 2:
            cnt += 1

    else:#k초과
        if array[left] % 2:
            cnt -= 1
        left += 1
print(result)