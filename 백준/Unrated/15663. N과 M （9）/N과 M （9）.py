import sys

input=sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
answer = []
store = []
index = []

def make():
    if len(answer) == M:
        word=" ".join(map(str, answer))
        if word not in store:
            store.append(word)
            print(word)
            return
        else:
            return

    for i in range(N):
        if i not in index:
            answer.append(arr[i])
            index.append(i)
            make()
            answer.pop()
            index.pop()

make()