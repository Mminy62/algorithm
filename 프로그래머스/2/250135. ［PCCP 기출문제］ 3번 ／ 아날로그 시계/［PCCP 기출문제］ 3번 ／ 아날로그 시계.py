def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 초침은 60으로 나눠지면 1초 지난 것, 1초에 1도씩 움직임
    # 
    # 시간을 전부 초로 바꿔서
    # 그 초의 움직임동안 마주치는 횟수
    time = (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1)
    sunit = s1 * 360 / 60
    munit = m1 * 360 / 60 + s1 * 360 / 60 / 60
    hunit = h1 * 360 / 12 + m1 * 360 / 12 / 60 + s1 * 360 / 12 / 60 / 60 
    
    # spre가 
    print(spre, mpre, hpre, spre + sunit, mpre + munit, hunit)
    for _ in range(time):
        

    return answer
'''

mAngle = m * 360 / 60 + s * 360 / 60 / 60 입니다.
시침은 분침의 현재 위치에 따라 360 / 12 안에서 위치가 결정 되고, 거기에 초침의 위치에 따라 360/12 / 60 안에서 위치가 결정 됩니다.
hAngle = h * 360 / 12 + m * 360 / 12 / 60 + s * 360 / 12 / 60 / 60 

'''