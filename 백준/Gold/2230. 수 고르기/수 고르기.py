n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
left, right = 0, 0

# 두 수의 차이가 M 이상이면서 제일 작은 수
result = int(2e9)

# 투 포인터 탐색 시작
while left <= right and right < n:

    # 두 수의 차이가 M 미만일 경우
    if arr[right]-arr[left] < m:
        # 오른쪽 인덱스를 1 증가
        right += 1
    elif arr[right]-arr[left] == m:
        result = m
        break
    # 두 수의 차이가 M 이상일 경우
    else:
        # 두 수의 차이가 M 이상이면서 제일 작은 수를 비교한 뒤, 업데이트
        result = min(result, arr[right]-arr[left])
        # 왼쪽 인덱스를 1 증가
        left += 1

# 결과 출력
print(result)