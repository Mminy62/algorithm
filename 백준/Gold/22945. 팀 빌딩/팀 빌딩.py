N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N - 1
result = 0
while start <= end:
    result = max(result, (end - start - 1) * min(arr[start], arr[end]))
    if arr[start] > arr[end]:
        end -= 1
    else:
        start += 1

print(result)