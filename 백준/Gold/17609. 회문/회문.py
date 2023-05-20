import sys
input = sys.stdin.readline
n = int(input())

lines = []
for _ in range(n):
    lines.append(input().strip())


for i in range(n):
    line = lines[i]
    if line == ''.join(reversed(line)):
        print(0)
        continue
    else:#유사 혹은 일반 문자열
        stack = []
        flag = 0
        size = len(line)
        for j in range(size//2):
            if line[j] != line[size-1-j]:
                stack.append(j)
                stack.append(size-1-j)
                break

        for s in stack:
            sen = list(line)
            del sen[s]
            if sen == list(reversed(sen)):
                print(1)
                stack = []
                flag = 1
                break

        if flag == 0:
            print(2)