#Stack
import sys

num = int(input()) #test case number

stack = []

for _ in range(num):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        command[1] = int(command[1])
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print("-1")
        else:
            top = stack.pop()
            print(top)

    elif command[0] == 'size':
        size = len(stack)
        print(size)

    elif command[0] == 'empty':
        if len(stack) == 0:
            print("1")
        else:
            print("0")
            
    else:#top
        if len(stack) == 0:
            print("-1")
        else:
            top = stack[-1]
            print(top)
