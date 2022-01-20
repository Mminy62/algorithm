
import sys

n = int(sys.stdin.readline())
data = []



for _ in range(n):
    data.append(list(sys.stdin.readline().rstrip()))


for d in data:
    count = 0
    result = 0
    for i in range(len(d)):
        if d[i] == 'O':
            count += 1
        else:
            count = 0
        result += count
        
    print(result)
