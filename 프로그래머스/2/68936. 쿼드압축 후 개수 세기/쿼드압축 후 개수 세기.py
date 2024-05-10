from collections import deque
cnt0 = 0
cnt1 = 0
def check(arr): # 둘다 있으면 False, 둘중에 하나라도 없으면 True
    global cnt0, cnt1
    
    n = len(arr)
    empty0 = True
    empty1 = True
#   각 배열을 검사하는 것
    for i in range(n):
        if 0 in arr[i]:
            empty0 = False
        if 1 in arr[i]:
            empty1 = False   
        
    if empty0 == True and empty1 == False:
        cnt1 += 1
    if empty0 == False and empty1 == True:
        cnt0 += 1
        
    return empty0 or empty1

def solution(arr):
    global cnt0, cnt1
    answer = []
    board = deque([arr])
    
    while board:
        arr = board.popleft()
    
        if not check(arr): # 0, 1 둘다 있는 경우만 받아서 4등분 하기
            n = len(arr) // 2
                
            # 4등분
            for i in range(0, len(arr), n):
                for j in range(0, len(arr), n):
                    temp = []
                    for x in range(i, i + n):
                        temp.append(arr[x][j: j + n])
                    board.append(temp)

    return [cnt0, cnt1]