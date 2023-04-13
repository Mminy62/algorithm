from itertools import permutations

n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]

result = list(permutations(nums, m))

for data in result:
    print(*data, sep=' ')