'''
원판 종류만 a, b, c
크기는 갖고 게임 시작시 다 0이상
각 막대에 a끼리만,
되도록 최소로 움직이기

# A 막대를 기준으로 원판이 B로 갈지 C로 가야될지
어떤 규칙을 써야 가장 최소로 가는 것인지 고민하는 시간이 길어져 결국 해설지를 봤다
다들 완탐으로 푼걸 보고 input을 확인했더니,
원판의 개수는 <=10 이고 막대는 3개이니 충분한 결과였다.

잘 모르겠는 경우엔 input의 개수를 확인하자!
너무 어려울 땐 완탐일 가능성이 높다
'''

from collections import deque

visited = set()
input1 = list(input().split())
s1 = input1[-1] if len(input1) > 1 else ''
input2 = list(input().split())
s2 = input2[-1] if len(input2) > 1 else ''
input3 = list(input().split())
s3 = input3[-1] if len(input3) > 1 else ''

queue = deque([])
queue.append((s1, s2, s3, 0))

while queue:
    a, b, c, count = queue.popleft()
    temp = a + '/' + b + '/' + c
    if temp in visited:
        continue

    if temp not in visited:
        visited.add(temp)

    if a == "A"*len(a) and b == "B"*len(b) and c == "C"*len(c):
        print(count)
        break

    # a에 A만 있는데도 옮기게 되는 것 같은데?..
    if len(a) > 0:
        queue.append((a[:-1], b + a[-1], c, count + 1))
        queue.append((a[:-1], b, c + a[-1], count + 1))
    if len(b) > 0:
        queue.append((a + b[-1], b[:-1], c, count + 1))
        queue.append((a, b[:-1], c + b[-1], count + 1))
    if len(c) > 0:
        queue.append((a + c[-1], b, c[:-1], count + 1))
        queue.append((a, b + c[-1], c[:-1], count + 1))