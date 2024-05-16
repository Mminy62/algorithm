def solution(n):
    answer = []
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    arr = []
    for i in range(1, n + 1):
        arr.append([0] * i)
    
    x, y = -1, 0
    di = 0
    num = 1
    final = (n * (n + 1)) // 2
    
    while num <= final:
        nx, ny = x + dx[di], y + dy[di]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
            di = (di + 1) % 3
            continue
        
        arr[nx][ny] = num
        num += 1
        x, y = nx, ny
    
    for i in range(n):
        answer += arr[i]
    
    return answer