word = list(input())
arr = [''] * len(word)
word_list = list(enumerate(word))
n = len(word)

for _ in range(n):
    temp = []
    for item in word_list:
        idx, value = item
        arr[idx] = value
        temp.append((''.join(arr), idx, value))
        arr[idx] = ''

    temp.sort()
    w, idx, value = temp[0]
    arr[idx] = value
    print(w)
    word_list.remove((idx, value))