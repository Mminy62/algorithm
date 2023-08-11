t = int(input())

for _ in range(t):
    callbook = []

    n = int(input())
    for _ in range(n):
        callbook.append(input())
    
    callbook.sort()
    
    for i in range(1, n):
        length = len(callbook[i-1])
        if callbook[i][:length] == callbook[i-1]:
            print('NO')
            break
    else:
        print('YES')
