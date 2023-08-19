n = int(input())
array = []
dicts = {}

for _ in range(n):
    temp = input()
    array.append(temp)
    for i in range(len(temp)):
        if temp[i] not in dicts:
            dicts[temp[i]] = 10 ** (len(temp) - i - 1)
        else:
            dicts[temp[i]] += 10 ** (len(temp) - i - 1)

dicts = sorted(dicts.items(), key = lambda item: item[1], reverse = True)

v = 9
new_dicts = {}
sens = [''] * n

for i, weigh in dicts:
    new_dicts[i] = v
    v -= 1

for i in range(n):
    for j in range(len(array[i])):
        sens[i] += str(new_dicts[array[i][j]])

result = 0
for i in range(n):
    result += int(sens[i])

print(result)