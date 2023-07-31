import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

# mod 값이 같은 배열 갯수 -> cnt[1] = 4 -> 나머지 값이 1인 prefix sum 이 4개
cnt = [0] * m
ans = 0
prefix = 0

for i in range(n):
    prefix += array[i]
    cnt[prefix % m] += 1

for i in range(m):
    ans += cnt[i] * (cnt[i]-1) // 2

ans += cnt[0]

print(ans)