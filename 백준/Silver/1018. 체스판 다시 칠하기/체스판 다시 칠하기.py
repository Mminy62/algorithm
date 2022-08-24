R, C = map(int,input().split(' '))

board = []
for i in range(R):
    board.append(list(input()))


def CountFix(r,c, start):

    fix = 0

    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if i % 2 == 0 and j % 2 == 0:  # even row and even col
                if board[i][j] != start:
                    fix += 1
            elif i % 2 != 0 and j % 2 != 0:  # odd row and odd col
                if board[i][j] != start:
                    fix += 1
            else:  # even row and odd col || odd row and even col
                if board[i][j] == start:
                    fix += 1

    return fix

fixcnt = []

for r in range(R-7):
    for c in range(C-7):
        tempFix = []
        tempFix.append(CountFix(r, c, board[r][c]))
        tempFix.append(CountFix(r, c, board[r][c+7]))
        tempFix.append(CountFix(r, c, board[r+7][c]))
        tempFix.append(CountFix(r, c, board[r+7][c+7]))

        fixcnt.append(min(tempFix))

print(min(fixcnt))

