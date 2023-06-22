k = int(input())
n = int(input())

array2 = list(input())

# 이차배열로 만들어서 사다리를 만나면 내려가기
ladder = []
line = 0
for index in range(n):
    row = list(input())
    if row[0] == '?':
        line = index
    ladder.append(row)

# 시작 배열
array = []
for i in range(k):
    array.append(chr(i + 65))

# 위에서부터 '?' 까지 사다리 타기
for i in range(line):
    for j in range(k-1):
        if ladder[i][j] == '-':
            array[j], array[j+1] = array[j+1], array[j]

# 밑에서부터 '?' 까지 사다리 타기
for i in range(n-1, line, -1):
    for j in range(k - 1):
        if ladder[i][j] == '-':
            array2[j], array2[j + 1] = array2[j + 1], array2[j]

# 이동 수 구하는 배열
temp = [0] * k
for i in range(k):
    for j in range(k):
        if array[i] == array2[j]:
            temp[i] = j-i

result = ''
for i in range(k):
    if abs(temp[i]) >= 2:
        result = 'x' * (k-1)
if not result:
    for i in range(k-1):
        if temp[i] != 0 and temp[i] + temp[i+1] == 0:
            result += '-'
            temp[i], temp[i+1] = 0, 0
        else:
            result += '*'

    if len(result) < k-1:
        result = 'x' * (k-1)

print(result)