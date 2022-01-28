import sys

N = sys.stdin.readline().rstrip()

word_list = []
for i in N:
    if i in 'ABC':
        word_list.append(3)
    elif i in 'DEF':
        word_list.append(4)
    elif i in 'GHI':
        word_list.append(5)
    elif i in 'JKL':
        word_list.append(6)
    elif i in 'MNO':
        word_list.append(7)
    elif i in 'PQRS':
        word_list.append(8)
    elif i in 'TUV':
        word_list.append(9)
    elif i in 'WXYZ':
        word_list.append(10)

print(sum(word_list))
