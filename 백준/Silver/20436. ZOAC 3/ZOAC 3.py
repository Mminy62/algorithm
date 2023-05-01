info = [
    [('q', 0), ('w', 0), ('e', 0), ('r', 0), ('t', 0), ('y', 1), ('u', 1), ('i', 1), ('o', 1), ('p', 1)],
    [('a', 0), ('s', 0), ('d', 0), ('f', 0), ('g', 0), ('h', 1), ('j', 1), ('k', 1), ('l', 1)],
    [('z', 0), ('x', 0), ('c', 0), ('v', 0), ('b', 1), ('n', 1), ('m', 1)]
]

left_chr = []
right_chr = []
left_pos = []
right_pos = []
for i in range(len(info)):
    for j in range(len(info[i])):
        if info[i][j][1] == 0:
            left_pos.append((i, j))
            left_chr.append(info[i][j][0])
        else:
            right_pos.append((i, j))
            right_chr.append(info[i][j][0])


cur_left, cur_right = input().split()
cur_left_pos, cur_right_pos = left_pos[left_chr.index(cur_left)], right_pos[right_chr.index(cur_right)]
strings = input()
time = 0

for s in strings:
    if s == cur_left:# 현재 위치와 문자가 다르면 찾아보기
        time += 1
    elif s == cur_right:
        time += 1

    else: # 현재 값이 아님
        if s in left_chr:
            x1, y1 = cur_left_pos
            x2, y2 = left_pos[left_chr.index(s)]
            cur_left = s
            cur_left_pos = (x2, y2)

        else:
            x1, y1 = cur_right_pos
            x2, y2 = right_pos[right_chr.index(s)]
            cur_right = s
            cur_right_pos = (x2, y2)

        time += abs(x1-x2) + abs(y1-y2) + 1


print(time)