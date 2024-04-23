def solution(dirs):
    answer = 0
    res = set()
    
    direct = {'U': (1, 0), 'D': (-1, 0), 'L': (0, 1), 'R': (0, -1)}
    x, y = 0, 0
    
    for i in range(len(dirs)):
        dx, dy = direct[dirs[i]]
        nx = x + dx
        ny = y + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        # 현재 & 나중 좌표를 정렬해서 넣고 길이 측정
        temp = sorted([(x, y), (nx, ny)])
        res.add(tuple(temp))
        x, y = nx, ny
    
    return len(res)