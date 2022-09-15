def calculate(w, h): #index 값
    
    
    return max(w) * max(h)


def solution(sizes):
    answer = 0
    #가로, 세로 기준 제일 큰 값이 있는 것만 눕혀서 보관하는 것도 생각해서 경우의 수를 따져 볼 것
    #바꾼 후 다시 돌리기
    wl = []
    hl = []
    
    for i in range(len(sizes)):
        w, h = sizes[i] # 큰 값을 wl  작은 값을 hl
        if h > w:
            wl.append(h)
            hl.append(w)
        else:
            wl.append(w)
            hl.append(h)
            
    
    answer = max(wl) * max(hl)

    
    return answer