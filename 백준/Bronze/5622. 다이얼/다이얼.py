from collections import defaultdict
word = input().rstrip()

dial = defaultdict(int)
num = 2
repeat = 3
c = 64
while num < 10:
    if num == 7 or num == 9:
        repeat = 4
    else:
        repeat = 3
    for _ in range(repeat):
        c += 1
        dial[chr(c)] = num

    num += 1

answer = 0
for s in word:
    answer += dial[s]

print(answer + len(word))




