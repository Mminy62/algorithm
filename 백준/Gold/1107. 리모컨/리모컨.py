'''
1. 현재에서 바로 특정번호로 점프한 후 -> 차이만큼 빼주는 것
    => 특정번호 길이 + 차이
    - 특정번호엔 고장난 번호가 들어있으면 안됨

2. 처음부터 올라가기
    => 목표와의 차이

'''

target = int(input())
m = int(input())

# 지금과의 차이
result = abs(target - 100)

if m == 0:
    result = min(result, len(str(target)))
else:
    broken = list(map(int, input().split()))

    for num in range(target + result + 1):
        number = str(num)

        for i in range(len(number)):
            if int(number[i]) in broken:
                break

            elif i == len(number)-1:
                result = min(result, abs(num-target) + len(number))

print(result)