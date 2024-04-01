import sys


# 투포인터 실행 함수
def two_pointer():
    global ans

    for i in range(N):
        for j in range(i + 3, N):
            s, e = i + 1, j - 1  # 투포인터를 돌릴 지점을 i 와 j의 사이로 잡아줍니다.
            while s < e:  # s 가 e 보다 작을때만 돈다.
                tmp = (arr[s] + arr[e]) - (arr[i] + arr[j])
                if abs(ans) > abs(tmp):  # 만약 절대값 차가 저장된 값보다 작다면
                    ans = abs(tmp)  # 그 값을 저장
                elif tmp == 0:  # 만약 0이라면 더이상 검사할 필요가 없으므로 
                    ans = 0  # 0을 저장하고
                    return  # 탈출

                if tmp > 0:  # 만약 tmp가 양수라면 더 커지면 안되기 때문에 끝인덱스를 한칸 땡긴다.
                    e -= 1
                else:  # 만약 tmp가 음수라면 더 작아지면 안되기 때문에 시작인덱스를 한칸 뒤로 민다.
                    s += 1


N = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 정렬
ans = sys.maxsize

two_pointer()  # 투포인터 함수 실행
print(ans)