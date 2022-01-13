import sys

data = {}

for i in range(9):
    index = int(sys.stdin.readline())
    data[index] = i


mdata = max(data.keys())
print(mdata)
print(data[mdata] + 1)
