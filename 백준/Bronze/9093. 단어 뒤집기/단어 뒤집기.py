n = int(input())
senten = []
result = []
for i in range(n):
    senten.append(input().split(' '))

for words in senten:
    result.append(map(lambda x: x[::-1], words))

for sen in result:
    print(*sen, sep = ' ')