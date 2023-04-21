n = int(input())
strings = input()
lines = list(strings)
cnt = 0

start = 0
if lines[0] == 'B':
    end = strings.rindex('B')
else:
    end = strings.rindex('R')
cnt += 1

if strings[start] == 'B':
    for i in range(start + 1, end):
        if lines[i - 1] != lines[i] and lines[i] == 'R':
            cnt += 1
else:
    for i in range(start + 1, end):
        if lines[i - 1] != lines[i] and lines[i] == 'B':
            cnt += 1

if end != n - 1:
    cnt += 1

print(cnt)