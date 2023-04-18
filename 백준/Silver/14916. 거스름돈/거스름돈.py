n = int(input())
cnt = 0
while n > 0:
    temp = n - 2
    if n % 5 == 0 and n >= 5:
        temp = n - 5
    cnt += 1
    n = temp

if n == 0:
    print(cnt)
else:
    print(-1)