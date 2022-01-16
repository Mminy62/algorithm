import sys


result = 1
data = [0] * 10

a = [int(sys.stdin.readline()) for _ in range(3)]

for i in a:
    result *= i

for i in str(result):
    data[int(i)] += 1

for i in data:
    print(i)
