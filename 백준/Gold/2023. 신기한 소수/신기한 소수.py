import math
n = int(input())

stack = []

def check(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False #num이 i의 배수면 소수가 아니므로 false
    return True

def dfs():
    if len(stack) == n:
        print(''.join(map(str, stack)))
        return

    for i in range(10):
        stack.append(i)
        if check(int(''.join(map(str, stack)))):
            dfs()
        # 소수가 아닌 경우
        stack.pop()
    return

first = [2, 3, 5, 7]

for f in first:
    stack.append(f)
    dfs()
    stack.pop()