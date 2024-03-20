import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
rules = []
for _ in range(K):
    rules.append(list(map(int, input().split())))

rules.sort()
start = 0
end = N
result = N + 1
# (end - start) // step + 1
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    #10 ** 4
    for rstart, rend, step in rules:
        if rstart > mid:
            continue

        if rend < mid:
            cnt += ((rend - rstart) // step + 1)

        else: # rstart < mid < rend
            cnt += ((mid - rstart) // step + 1)

    if cnt >= D:
        result = min(result, mid)
        end = mid - 1
    else:
        start = mid + 1

print(result)