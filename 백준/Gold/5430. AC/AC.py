import sys
input = sys.stdin.readline


tc = int(input())
result = []
for _ in range(tc):
    cmds = input().rstrip()
    length = int(input())
    stack = input().rstrip()[1:-1].split(',')
    flag = True

    if cmds.count('D') > length:
        result.append('error')

    else:
        if 'RR' in cmds:
            cmds = cmds.replace('RR', '')

        for i in range(len(cmds)):

            if cmds[i] == 'R':
                flag = not flag

            else:#'D'
                if flag:
                    del stack[0]
                else:
                    del stack[-1]
        

        if flag:
            result.append('[' + ','.join(stack) + ']')
        else:
            result.append('[' + ','.join(stack[::-1]) + ']')
            


for k in result:
    print(k)