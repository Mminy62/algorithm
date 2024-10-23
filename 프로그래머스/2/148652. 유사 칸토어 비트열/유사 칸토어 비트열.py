'''
문자열의 길이가 최대 5 ** 20 이므로, 이 문제는 O(N)이 아닌 O(logN) 으로 풀어야한다. 
n 번째 비트열은 5개의 구간으로 나눌 수 있도록 일정한 규칙을 갖는다. 
n = 1, 11011 => 4
n = 2, 11011 11011 00000 11011 11011 => 16
n = 2 일때를 잘 살펴보면, (n - 1) 번째 비트열 | (n - 1) 번째 비트열 | 00000 | (n - 1) 번째 비트열 | (n - 1) 번째 비트열
임을 알 수 있다. 
각 구간은 5 ** (n - 1)의 비트를 갖고 있다.
또 n에 대한 1의 개수로는 4 ** (n) 개의 1의 수를 갖고 있다.

위와 같은 전개로 봤을 때, n = 2일 때의 비트열을 보면 (n - 1) 비트열과 밀접하다는 것을 알 수 있다. 
따라서 n일때의 비트열을 n - 1로 점차 이동해서 가장 작은 단계일 때로 반환하는 재귀함수를 이용한다. 

먼저 f(n, k) = "n번째 비트열에서 k번째까지의 1의 개수"를 의미
위 함수를 활용하면, 
f(n, r) - f(n, l - 1) = l ~ r 사이의 1의 개수가 된다. 

k의 구역을 5개의 구역으로 나누고 해당 구역을 loc이라고 했을 때
f(n, k) = f(n - 1, k - (loc 전 까지의 비트수)) + (loc - 1 까지의 1의 개수)


'''

def f(n, k):
    if n == 1:
        return k if k <= 2 else k - 1
    
    loc_size = 5 ** (n - 1)
    loc_1count = 4 ** (n - 1)
    loc = k // loc_size
    
    if k % loc_size == 0:
        loc -= 1
    
    if loc < 2:
        return loc * loc_1count + f(n - 1, k - loc * loc_size)
    elif loc == 2:
        return loc * loc_1count
    else:
        return (loc - 1) * loc_1count + f(n - 1, k - loc * loc_size)
    

def solution(n, l, r):
    answer = 0
    print()
    return f(n, r) - f(n, l - 1)