from collections import defaultdict

n = int(input())
dic = defaultdict(list)
for _ in range(n):
    name = input().split(".")
    key = name[1]
    value = name[0]

    dic[key].append(value)

for key in sorted(dic.keys()):
    print(key, len(dic[key]))