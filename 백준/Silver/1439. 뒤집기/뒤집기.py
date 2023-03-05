n = list(map(int, input()))
before = n[0]
first = n[0]
cnt = 0

for data in n:
    if before != data:
        if before == first:
            cnt += 1
        before = data

print(cnt)