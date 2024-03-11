H, W = map(int, input().split())
walls = list(map(int, input().split()))
array = [[0] * W for _ in range(H)]

for i in range(W):
    if walls[i]:#0이상이면
        for r in range(0, walls[i]):
            array[r][i] = 1

result = 0
for c in range(W):
    for r in range(H):
        count = 0
        if array[r][c] and c + 1 < W:
            nx = r
            ny = c + 1
            while array[nx][ny] != 1:# 1이면 멈추고 count 더하기
                count += 1
                ny += 1
                if ny > W - 1:
                    count = 0
                    break
        result += count

print(result)