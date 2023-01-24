n = input()

front = list(map(int, n[0:len(n)//2]))
back = list(map(int, n[len(n)//2:]))

if sum(front) == sum(back):
    print('LUCKY')
else:
    print('READY')