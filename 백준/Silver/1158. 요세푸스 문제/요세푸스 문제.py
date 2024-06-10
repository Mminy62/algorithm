n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
result = []
idx = -1
while arr:
    idx += k
    idx %= len(arr)
    result.append(arr[idx])
    del arr[idx]
    idx -= 1

ans = "<" + ', '.join(map(str, result)) + ">"
print(ans)