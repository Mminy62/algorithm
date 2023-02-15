n = int(input())
m = n
array = []

for i in range(n):
    array.append(list(map(int, input().split())))


def dp(array):

    if n == 1:
        return array[0]

    for i in range(n - 2, -1, -1):  # 3 2 1 0 # row
        for j in range(i, -1, -1):  # 4 3 2 1 0 -> 3 2 1 0 -> 2 1 0 # col

            left_down = array[i][j] + array[i + 1][j]
            right_down = array[i][j] + array[i + 1][j + 1]

            array[i][j] = max(left_down, right_down)


    return array[0]

print(*dp(array))
