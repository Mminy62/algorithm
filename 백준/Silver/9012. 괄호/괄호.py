import sys
n = int(sys.stdin.readline().rstrip())
tests = []
result = []

for _ in range(n):
    tests.append(list(sys.stdin.readline().rstrip()))

for line in tests:
    stack = []
    for w in line:
        if w == '(' or not bool(stack):
            stack.append(w)
        else:# w is ')' and not empty stack
            top = stack[-1]
            if top == '(':
                stack.pop()
            else:
                stack.append(w)
  
    if len(stack) > 0:
        result.append("NO")
    else:
        result.append("YES")

for _ in result:
    print(_)