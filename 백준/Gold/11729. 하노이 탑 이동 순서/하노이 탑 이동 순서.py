n = int(input())
cnt = 0
result = []
def move(start, end):
    global cnt, result
    result.append((start, end))
    cnt += 1
    return


def hanoi(N, start, via, end):
    if N == 1:
        move(start, end)
        return
    else:
        hanoi(N - 1, start, end, via)
        move(start, end)
        hanoi(N - 1, via, start, end)


hanoi(n, 1, 2, 3)
print(cnt)
for item in result:
    print(' '.join(map(str,item)))