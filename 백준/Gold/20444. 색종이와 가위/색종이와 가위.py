n, k = map(int, input().split())

start = 0
end = n//2
ans = 'NO'
while start <= end:
    mid = (start + end) // 2

    total = (mid + 1) * (n - mid + 1)
    if total == k:
        ans = 'YES'
        break
    elif total < k:
        start = mid + 1
    else:
        end = mid - 1

print(ans)