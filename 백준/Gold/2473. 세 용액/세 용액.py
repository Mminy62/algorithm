N = int(input())
waters = list(map(int, input().split()))

waters.sort()
result = 4e9
temp = []
flag = False

for i in range(N-2):
    start = i + 1
    end = N - 1
    fix = i

    while start < end:
        value = waters[start] + waters[end] + waters[fix]
        if abs(value) < result:
            result = abs(value)
            temp = [start, end, fix]

        if value > 0:
            end -= 1
        elif value < 0:
            start += 1
        else:
            flag = True
            break
    if flag:
        break

ans = []
for idx in sorted(temp):
    ans.append(str(waters[idx]))

print(' '.join(ans))