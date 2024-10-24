def checkBingo(grid, letter):
    cnt1, cnt2, cnt3 = 0, 0, 0
    bingo = 0
    
    # 행 체크
    for i in range(3):
        if grid[i][0] == letter and grid[i][1] == letter and grid[i][2] == letter:
            bingo += 1
    
    # 열 체크 수정
    for i in range(3):
        if grid[0][i] == letter and grid[1][i] == letter and grid[2][i] == letter:
            bingo += 1
    
    # 대각선 체크
    cnt1, cnt2 = 0, 0
    for i in range(3):
        if grid[i][i] == letter:
            cnt1 += 1
        if grid[i][2-i] == letter:
            cnt2 += 1
    
    if 3 in [cnt1, cnt2]:
        bingo += 1
    
    if bingo:
        return True
    
    return False

def solution(board):
    answer = -1
    grid = []
    for line in board:
        grid.append(list(line))
    
    ocount = 0
    xcount = 0
    for i in range(3):
        ocount += board[i].count("O")
        xcount += board[i].count("X")
    
    oBingo = checkBingo(grid, "O")
    xBingo = checkBingo(grid, "X")
    
    if oBingo and xBingo: # 둘다 빙고가 나오면 안됨
        return 0
    
    if not (ocount - xcount == 0 or ocount - xcount == 1):
        return 0
    
    if oBingo:
        if ocount <= xcount:
            return 0

    if xBingo:
        if ocount != xcount:
            return 0
    
    return 1