from collections import deque

def solution(land):
    answer = 0
    N, M = len(land), len(land[0])
    visited = [[False] * M for _ in range(N)]
    index = 2
    info = {}
    
    def bfs(x, y): # 덩어리 표시와 동시에 덩어리 갯수 return 
        N, M = len(land), len(land[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        cnt = 1
        visited[x][y] = True
        land[x][y] = index
        q = deque([(x, y)])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if land[nx][ny] == 0:
                    continue
                if land[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    land[nx][ny] = index
                    cnt += 1
                    q.append((nx, ny))
                
        return cnt

    #bfs 로 각 영역 크기 찾기
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and not visited[i][j]:
                count = bfs(i, j)
                info[index] = count
                index += 1
    
    info[0] = 0
    result = 0
    for j in range(M):
        tempSet = set()
        for i in range(N):
            tempSet.add(land[i][j])
            
        temp = 0
        for key in tempSet:
            temp += info[key]
        result = max(result, temp)
    
    return result