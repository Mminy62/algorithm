import itertools

def rotate_matrix(keys):
    n = len(keys)
    matrix = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[j][n-1-i] = keys[i][j]

    return matrix

def check(matrix):
    #원래의 자물쇠 길이
    lock_length = len(matrix)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if matrix[i][j] != 1:
                return False
    return True



def solution(key, lock):
    answer = False

    #열쇠 돌기의 수가 자물쇠의 구멍보다 작은 경우 (아예 못채우는 경우)
    if list(itertools.chain(*key)).count(1) < list(itertools.chain(*lock)).count(0):
        return False

    n = len(lock)
    m = len(key)

    temp_matrix = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            temp_matrix[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate_matrix(key)

        for x in range(n * 3 - m):
            for y in range(n * 3 - m):
                for i in range(m):
                    for j in range(m):
                        temp_matrix[x+i][y+j] += key[i][j]

                if check(temp_matrix):
                    return True
                else:#False
                    for i in range(m):
                        for j in range(m):
                            temp_matrix[x + i][y + j] -= key[i][j]

    return answer