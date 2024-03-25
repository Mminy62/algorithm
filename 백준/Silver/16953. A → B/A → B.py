A, B = map(int, input().split())

cnt = 0
#top-down 방식
while B > A:
    cnt += 1
    temp = B

    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    if temp == B:
        break

if B != A:
    print(-1)
else:
    print(cnt + 1)