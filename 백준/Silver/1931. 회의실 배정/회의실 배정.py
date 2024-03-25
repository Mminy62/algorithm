N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

# 한 회의실을 최대 몇개가 사용할 수 있는지 확인

arr.sort(key=lambda x: (x[1], x[0]))
end = arr[0][1]
cnt = 1
for i in range(1, N):
    if arr[i][0] >= end:
        end = arr[i][1]
        cnt += 1

print(cnt)