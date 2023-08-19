S = list(input())
T = list(input())

result = 0

while len(S) < len(T):

    if T[-1] == 'A':
        del T[-1]
    else:
        del T[-1]
        T = T[::-1]

if S == T:
    result = 1
print(result)