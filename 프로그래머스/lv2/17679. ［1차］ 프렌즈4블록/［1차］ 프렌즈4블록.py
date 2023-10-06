from collections import deque
def solution(m, n, board):
    answer = 0
    array = []

    for i in range(m):
        array.append(list(board[i]))
    
    dx = [0, 1, 1] # 현재칸이 있으면
    dy = [1, 0, 1]
    
    while True:
        # 삭제할 요소 탐색
        delete = deque([])

        for x in range(m-1):
            for y in range(n-1):
                pos = [(x, y)]
                if array[x][y] != "-": # 빈 상태가 아니면
                    for i in range(3):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if array[nx][ny] == array[x][y]:
                            pos.append([nx, ny])

                    if len(pos) == 4: # 4개 같은 문자 # 바로 없앨 수 없음 겹치는 것도 있기에
                        for _ in range(4):
                            px, py = pos.pop()
                            if (px, py) not in delete:
                                delete.append((px, py))

                #빈 문자면 패스

        if not delete: # 삭제 없으면 while문 탈출
            break
        # 요소 삭제
        for x, y in delete:
            array[x][y] = "-"

        # # 요소 내리기 
        for x in range(m-2, -1, -1):
            for y in range(n):
                if array[x][y] != "-" and array[x+1][y] == "-":
                    nx = x + 1
                    while nx < m and array[nx][y] == "-":
                        nx += 1
                    array[nx-1][y] = array[x][y]
                    array[x][y] = "-"
    
    # 삭제 갯수 세기
    for i in range(m):
        for j in range(n):
            if array[i][j] == "-":
                answer += 1
        
    return answer