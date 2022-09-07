n, k = map(int, input().split(' '))

scores = list(map(int, input().split(' ')))

scores.sort() #원본 수정

print(scores[-k])