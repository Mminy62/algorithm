n, m = map(int, input().split())

array = list(map(int, input().split()))
prefix = [0] * n
prefix[0] = array[0]

# 누적합 배열 생성
for i in range(1, n):
    prefix[i] = prefix[i-1] + array[i]

# mod 값이 같은 배열 갯수 -> cnt[1] = 4 -> 나머지 값이 1인 prefix sum 이 4개
cnt = [0] * m
ans = 0

for i in range(n):
    cnt[prefix[i] % m] += 1

for i in range(m):
    ans += cnt[i] * (cnt[i]-1) // 2

ans += cnt[0]

print(ans)