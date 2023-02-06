n = int(input())
score_list = []
for _ in range(n):
    temp = input().split()
    temp[1:] = map(int, temp[1:])
    score_list.append(temp)


score_list.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for data in score_list:
    print(data[0])