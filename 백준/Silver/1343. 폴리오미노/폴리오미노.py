board = input()
board = board.replace('XX', 'BB')
board = board.replace('BBBB', 'AAAA')

if 'X' in board:
    print(-1)
else:
    print(board)