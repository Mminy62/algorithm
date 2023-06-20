import sys
input = sys.stdin.readline

attends = []

for _ in range(28):
    attends.append(int(input()))


for i in range(1, 31):
    if i not in attends:
        print(i)