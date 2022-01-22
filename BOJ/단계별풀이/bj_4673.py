def d(n):
    nlist = list(map(int, str(n)))
    n = n + sum(nlist)
    return n


notselfnum = set()

for i in range(1, 10001):
    notselfnum.add(d(i))

for i in range(1, 10001):
    if i not in notselfnum:
        print(i)
        
        
'''
처음엔 재귀함수를 통해 모든 경우의 수를 다 뽑아 중복을 제거하여 더했지만, 
어차피 1부터 10000까지 모든 수를 d(n)에 넣는 이상
재귀함수를 통해 나온 값까지도 포함된 경우의 수 이기에
모든 수의 경우를 다 함수에 넣고 돌리는 선형의 방법이 시간을 확 줄여줬다. 
그리고 set()자체로 변수 초기화가 가능한지 몰랐었음.
'''
'''
<처음 코드>
notself = []

def d(n):
    result = n
    nlist = list(map(int, str(n)))
    for temp in nlist:
        result += temp

    if result > 10000:
        return 0
    else:
        d(result)
        self.append(result)

for i in range(1, 10001):
    d(i)

self = set(notself)

for i in range(1, 10001):
    if i not in notself:
        print(i)
'''
