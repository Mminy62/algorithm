import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    cmds = list(input().split())
    cmd = cmds[0]
    if cmd == "push":
        stack.append(int(cmds[1]))
    elif cmd == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif cmd == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    else:
        if not stack:
            print(1)
        else:
            print(0)