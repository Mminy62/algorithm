from copy import deepcopy
from collections import deque

L, Q = map(int, input().split())

def moving(desk, time):
    keys = desk.keys()
    for name in keys:
        n = len(desk[name])
        # 시간에 따라 아이템의 테이블 번호를 매겨
        for i in range(n):
            gap = time - desk[name][i][0]
            desk[name][i][0] = time
            # 이전 item이 있던 table 번호 저장
            desk[name][i][2] = desk[name][i][1]
            desk[name][i][3] = gap
            desk[name][i][1] = (desk[name][i][1] + gap) % L

    return desk

def eating(person, desk):
    # person 기준으로
    # 사람이 있으면
    q = deque(list(person.keys()))  # 동일인물 여러명 안나옴
    remove_list = set()
    while q:  # 사람 있다는 것
        name = q.popleft()
        person_time, person_table, person_n = person[name]

        # desk 자기 이름에 가서 번호랑 시간이 맞으면 먹기
        if name not in desk.keys():
            continue
        temp = deepcopy(desk[name])
        # print(temp)
        for item_time, item_x, item_prex, item_move_cnt in temp:
            if person_n > 0 and item_x == person_table:
                desk[name].remove([item_time, item_x, item_prex, item_move_cnt])
                person[name][2] -= 1
            if person_n > 0 and item_x != person_table:
                temp = item_prex + item_move_cnt

                if person_table == 0:
                    if temp // L > 0:
                        desk[name].remove([item_time, item_x, item_prex, item_move_cnt])
                        person[name][2] -= 1
                else:# 사람의 테이블 번호가 양수일 땐
                    # 나보다 크거나 같을때
                    if item_prex <= person_table and person_table <= temp:
                        desk[name].remove([item_time, item_x, item_prex, item_move_cnt])
                        person[name][2] -= 1
            if person_n == 0:
                continue
    # n이 0된사람 지우기
    temp_p = deepcopy(person)
    for name, item in temp_p.items():
        if item[-1] == 0:
            del person[name]
    temp_d = deepcopy(desk)
    for name, item in temp_d.items():
        if name not in desk.keys():
            continue
        if not item:
            del desk[name]


    return (person, desk)

def count(person, desk):
    person_cnt = len(person.keys())
    desk_cnt = 0

    for key, values in desk.items():
        desk_cnt += len(values)

    return [person_cnt, desk_cnt]


desk = {}
person = {}
photos = []

for _ in range(Q):
    cmd = list(input().split())
    if cmd[0] == '100':# t, x, name
        # desk 움직임
        t, x, name = cmd[1:]
        t, x = int(t), int(x)
        desk = moving(desk, t)

        if name not in desk.keys(): #(t, x)
            desk[name] = [[t, x, x, 0]]
        else:
            desk[name].append([t, x, x, 0])

        person, desk = eating(person, desk)

    if cmd[0] == '200':# t, x, name, n개
        t, x, name, n = cmd[1:]
        t, x, n = int(t), int(x), int(n)
        person[name] = [t, x, n]
        desk = moving(desk, t)
        person, desk = eating(person, desk)

    if cmd[0] == '300': # t
        t = int(cmd[1])
        desk = moving(desk, t)
        person, desk = eating(person, desk)
        print(' '.join(map(str, count(person, desk))))



