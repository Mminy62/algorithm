def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # 시작시간과 끝시간을 초단위로 변환
    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2
    
    spre = s1 * 360 / 60
    mpre = m1 * 360 / 60 + s1 * 360 / 60 / 60
    hpre = h1 * 360 / 12 + m1 * 360 / 12 / 60 + s1 * 360 / 12 / 60 / 60 
    
    if startTime == 0 * 3600 or startTime == 12 * 3600:
        answer += 1
        
            
    for time in range(startTime, endTime): # 처음시간 체크
        hpre = time / 120 % 360
        mpre = time / 10 % 360
        spre = time * 6 % 360
        
        # 다음 위치가 360도가 아닌 0도로 계산되어 카운팅에 포함되지 않는 경우 방지
        # 이동했을 때 지나쳤거나 같아졌는지를 비교하는 것이므로 현재위치는 해줄 필요없음
        hpost = 360 if (time + 1) / 120 % 360 == 0 else (time + 1) / 120 % 360
        mpost = 360 if (time + 1) / 10 % 360 == 0 else (time + 1) / 10 % 360
        spost = 360 if (time + 1) * 6 % 360 == 0 else (time + 1) * 6 % 360

        if (spre < mpre and mpost <= spost):
            answer += 1

        if (spre < hpre and hpost <= spost):
            answer += 1
        
        if mpost == hpost and spost == mpost:
            answer -= 1
        
        spre, mpre, hpre = spost, mpost, hpost


    return answer