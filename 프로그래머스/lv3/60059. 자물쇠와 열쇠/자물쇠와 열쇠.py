# import itertools

# def rotate_matrix(keys):
#     n = len(keys)
#     matrix = [[0] * n for i in range(n)]

#     for i in range(n):
#         for j in range(n):
#             matrix[j][n-1-i] = keys[i][j]

#     return matrix

# def check(matrix):
#     #원래의 자물쇠 길이
#     lock_length = len(matrix)//3
#     for i in range(lock_length, lock_length*2):
#         for j in range(lock_length, lock_length*2):
#             if matrix[i][j] != 1:
#                 return False
#     return True



# def solution(key, lock):
#     answer = False

#     #열쇠 돌기의 수가 자물쇠의 구멍보다 작은 경우 (아예 못채우는 경우)
#     if list(itertools.chain(*key)).count(1) < list(itertools.chain(*lock)).count(0):
#         return False

#     n = len(lock)
#     m = len(key)

#     temp_matrix = [[0] * (n * 3) for _ in range(n * 3)]

#     for i in range(n):
#         for j in range(n):
#             temp_matrix[i+n][j+n] = lock[i][j]

#     for _ in range(4):
#         key = rotate_matrix(key)

#         for x in range(n * 3 - m):
#             for y in range(n * 3 - m):
#                 for i in range(m):
#                     for j in range(m):
#                         temp_matrix[x+i][y+j] += key[i][j]

#                 if check(temp_matrix):
#                     return True
#                 else:#False
#                     for i in range(m):
#                         for j in range(m):
#                             temp_matrix[x + i][y + j] -= key[i][j]

#     return answer

def rotate_key(key, m):
    graph = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            graph[j][m-i-1] = key[i][j]

    return graph

def check(matrix, n):

    # matrix 가운데 자물쇠 부분
    for i in range(n, n + n):
        for j in range(n, n + n):
            if matrix[i][j] != 1:
                return False
    return True

def solution(key, lock):
    # key - m, lock - n
    # m <= n 항상 ## lock의 크기가 더 크다 ## 시간복잡도 n으로 계산한 거니까 괜춘
    # 0 이 홈 1이 돌기 ## 가운데 부분이 전부 1이면 통과
    m = len(key)
    n = len(lock)

    #lock 의 9배 크기의 matrix 생성
    matrix = [[0] * n * 3 for _ in range(n * 3)]

    # matrix 가운데에 Lock으로 초기화
    for i in range(n, n + n):
        for j in range(n, n + n):
            matrix[i][j] = lock[i-n][j-n]

    for i in range(4):
        key = rotate_key(key, m)

        # key의 matrix 이동
        for r in range(0, n * 2 + 1):
            for c in range(0, n * 2 + 1):

                for i in range(m):
                    for j in range(m):
                        matrix[i + r][j + c] += key[i][j]

                if not check(matrix, n):  # 틀리면
                    for i in range(m):
                        for j in range(m):
                            matrix[i + r][j + c] -= key[i][j]
                else:
                    return True

    return False
