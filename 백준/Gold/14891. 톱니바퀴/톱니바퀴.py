from collections import deque
array = deque([])
for _ in range(4):
    array.append(deque(list((map(int, input().rstrip())))))

m = int(input())
cmd = deque([])
for _ in range(m):
    n, d = map(int, input().split())
    cmd.append((n-1, d))

def rotate(r):
    while r:
        num, direct = r.popleft()
        array[num].rotate(direct)

    return


while cmd:
    node, d = cmd.popleft()
    check = deque([(node, d)])
    temp = deque([(node, d)])
    visited = [False] * 4

    while temp:
        num, direct = temp.popleft()
        visited[num] = True

        if num - 1 >= 0 and not visited[num - 1] and array[num-1][2] != array[num][6]:
            check.append((num-1, direct * (-1)))
            temp.append((num-1, direct * (-1)))
        if num + 1 < 4 and not visited[num + 1] and array[num + 1][6] != array[num][2]:
            check.append((num+1, direct * (-1)))
            temp.append((num+1, direct * (-1)))

    rotate(check)

result = 0
for i in range(4):
    if array[i][0]:
        result += 2 ** i

print(result)