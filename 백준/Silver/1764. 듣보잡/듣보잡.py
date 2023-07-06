import sys
input = sys.stdin.readline

n, m = map(int, input().split())

see = []
listen = []
for _ in range(n):
    see.append(input().rstrip())

for _ in range(m):
    listen.append(input().rstrip())

see.sort()
listen.sort()
result = []

def binary_search(array, item, length):
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == item:
            return True
        elif array[mid] < item:
            start = mid + 1
        else:
            end = mid - 1

    return False

if n < m:
    # listen 기준 탐색
    for i in range(n):
        if binary_search(listen, see[i], m):
            result.append(see[i])
else:
    for i in range(m):
        if binary_search(see, listen[i], n):
            result.append(listen[i])

print(len(result))
print('\n'.join(result))