n = int(input())
k = int(input())
cnt = 0

# value 를 기준으로
'''
https://st-lab.tistory.com/281
'''

s = 1
e = n ** 2
result = 0

while s < e:
    cnt = 0
    mid = (s + e)//2

    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        e = mid
        result = mid
    else:
        s = mid + 1

print(s)