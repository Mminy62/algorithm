from collections import deque

T = int(input())
for _ in range(T):
    cmds = input()
    cmds = cmds.replace("RR", "")
    n = int(input())
    temp = input()
    arr = deque([])
    if n:
        arr = deque(list(map(int, temp[1:-1].split(","))))

    flag = True

    # 연산
    answer = ""
    for c in cmds:
        if c == "R":
            flag = not flag
        else:
            if not arr:
                answer = "error"
                break
            if flag:
                arr.popleft()
            else:
                arr.pop()

    if answer != "error":
        if not arr:
            answer = "[]"
        elif flag:
            answer = "[" + ','.join(map(str, arr)) + "]"
        else:
            answer = "[" + ','.join(map(str, reversed(arr))) + "]"

    print(answer)