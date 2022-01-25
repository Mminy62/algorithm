import sys

data = sys.stdin.readline().rstrip().split(' ')
re_data = []
for i in range(2):
    re_data.append(int(''.join(reversed(data[i]))))

print(max(re_data))
