L, C = map(int, input().split())

array = list(input().split())
array.sort()

result = []
def check(sen):
    cnt = 0
    flag = False
    for i in range(len(sen)):
        if sen[i] in ['a', 'e', 'i', 'o', 'u']:
            flag = True
        else:
            cnt += 1

    if cnt >= 2 and flag:
        return True

    return False

def dfs(s):
    if len(result) == L and check(result):
        print(''.join(result))
        return

    for i in range(s, C):
        if array[i] not in result:
            result.append(array[i])
            dfs(i)
            result.pop()

    return

dfs(0)