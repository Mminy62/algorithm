n = int(input())
words = []

for _ in range(n):
    words.append(input())

words = sorted(list(set(words)))
words.sort(key=len)

for i in words:
    print(i)