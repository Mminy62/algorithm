from functools import cmp_to_key

# 주의할 점 ->  cmp_to_key의 return 값: 음수/0/양수 ## not bool

n = int(input())
array = []
for _ in range(n):
    array.append(input().rstrip())

def to_list(word):
    li = list(word)
    i = 0
    while i < len(li):
        if li[i].isdigit():
            end = i
            while end < len(li) and li[end].isdigit():
                end += 1
            li[i:end] = [''.join(li[i:end])]
            i = end - 1
        i += 1
    return li


def diff(w1, w2):
    w1 = to_list(w1)
    w2 = to_list(w2)

    i = 0

    while i < min(len(w1), len(w2)):
        if w1[i] == w2[i]:
            i += 1
            continue
        # 숫자 & 문자 비교
        if w1[i].isalpha() and w2[i].isdigit():
            return 1
        elif w1[i].isdigit() and w2[i].isalpha():
            return -1

        # 문자 & 문자 일 때
        if w1[i].isalpha() and w2[i].isalpha():
            if w1[i].lower() == w2[i].lower(): ## ex) B b
                return -1 if w1[i] < w2[i] else 1
            return -1 if w1[i].lower() < w2[i].lower() else 1 # 두 문자가 다른 것 ex. a c
        #숫자 & 숫자 일 때
        if w1[i].isdigit() and w2[i].isdigit():
            if int(w1[i]) == int(w2[i]):
                return -1 if len(w1[i]) < len(w2[i]) else 1
            return -1 if int(w1[i]) < int(w2[i]) else 1
        i += 1
    if len(w1) == len(w2):
        return 0
    return -1 if len(w1) < len(w2) else 1


array.sort(key=cmp_to_key(diff))

for s in array:
    print(s)