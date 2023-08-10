N, M = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

blocks = []
# 긴 블럭
blocks.append([(0, 0), (0, 1), (0, 2), (0, 3)])
blocks.append([(0, 0), (1, 0), (2, 0), (3, 0)])
# 네모 블럭
blocks.append([(0, 0), (1, 0), (0, 1), (1, 1)])
# 복잡 블럭
blocks.append([(0, 0), (1, 0), (1, 1), (2, 1)])
blocks.append([(0, 0), (0, 1), (-1, 1), (-1, 2)])
blocks.append([(0, 0), (0, 1), (1, 1), (1, 2)])
blocks.append([(0, 0), (1, 0), (1, -1), (2, -1)])
# 우 블럭
blocks.append([(0, 0), (0, 1), (0, 2), (1, 1)])
blocks.append([(0, 0), (0, 1), (0, 2), (-1, 1)])
blocks.append([(0, 0), (1, 0), (2, 0), (1, 1)])
blocks.append([(0, 0), (1, 0), (2, 0), (1, -1)])
# 니은 블럭
blocks.append([(0, 0), (1, 0), (2, 0), (2, 1)])
blocks.append([(0, 0), (-1, 0), (-2, 0), (-2, 1)])
blocks.append([(0, 0), (0, 1), (0, 2), (-1, 2)])
blocks.append([(0, 0), (-1, 0), (-2, 0), (-2, -1)])
blocks.append([(0, 0), (0, -1), (0, -2), (1, -2)])
blocks.append([(0, 0), (0, 1), (0, 2), (1, 2)])
blocks.append([(0, 0), (1, 0), (2, 0), (2, -1)])
blocks.append([(0, 0), (0, -1), (0, -2), (-1, -2)])

result = 0
for x in range(N):
    for y in range(M):
        for block in blocks:
            temp = 0
            for i in range(4):
                nx = x + block[i][0]
                ny = y + block[i][1]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                temp += maps[nx][ny]
            # block 한개 끝나면 비교
            result = max(result, temp)

print(result)