n = int(input())
number = int(input())

square = 0
x = 1
y = 1
key = 0
for i in range(n, 0, -2):
    if i * i < number:
        square = i * i
        key = i
        break
    x += 1
    y += 1
if key == 0:
    square, key = 1, 1

def find_pos(square, x, y, key):
    dx = [1, 0, -1]
    dy = [0, -1, 0]
    # key 부터 순차대로 수를 알아간다. # 오른쪽, 아래, 왼, 위
    # 처음 1번은 위로, 오른쪽으로 가는건 n번 더하기
    for i in range(1, key + 2):
        if i == 1:
            square += 1
            x -= 1
        else:
            square += 1
            y += 1

        if square == number:
            return (x, y)
    #아래, 왼쪽, 위로 가는 방향 한줄 탐색
    for i in range(3):
        for j in range(1, key + 2):
            square += 1
            x += dx[i]
            y += dy[i]
            if square == number:
                return (x, y)

    return (x, y)


def draw(n):
    x, y = n//2 + 1, n//2 + 1
    num = 2
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    matrix = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n, 2):  # 1000 * 4 * 1000 4백만
        for i in range(4):
            for j in range(length):
                if i == 0 and j == 0:
                    x -= 1
                else:
                    x += dx[i]
                    y += dy[i]

                matrix[x][y] = num
                num += 1
    return matrix

result = draw(n)
result[n//2 + 1][n//2 + 1] = 1
for r in range(1, n + 1):
    print(*result[r][1:])

print(*find_pos(square, x, y, key))
