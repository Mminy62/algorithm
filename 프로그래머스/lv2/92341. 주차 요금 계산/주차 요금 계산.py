from datetime import datetime 
import math

def solution(fees, records):
    answer = []
    carNum = {}
    
    for data in records:
        re_time, re_car, re_inout = data.split(' ')
        
        if re_inout == "IN":
            if re_car not in carNum.keys():
                carNum[re_car] = [re_time]
            else: # 입출차 경험이 있는 차 만약에 re_time 의 수가 홀수면 마지막은 무조건 안나간거
                carNum[re_car].append(re_time)
        else:#"OUT"
            carNum[re_car].append(re_time)

    for key, values in carNum.items():
        parktime = 0
        
        for i in range(0, len(values)-1, 2): #4: 0, 2
                time_1 = datetime.strptime(values[i], "%H:%M")
                time_2 = datetime.strptime(values[i+1], "%H:%M")
                
                time_interval = round((time_2-time_1).seconds / 60)
                
                parktime += time_interval
            
        if len(values) % 2 != 0: #홀수면 출차 안한 차 더 계산
            time_1 = datetime.strptime(values[-1], "%H:%M")
            time_2 = datetime.strptime('23:59', "%H:%M")
            time_interval = round((time_2-time_1).seconds / 60)
            parktime += time_interval
        
        carNum[key] = parktime
            
    for k, v in sorted(carNum.items()):#요금 계산
        if v > fees[0]:
            result = fees[1] + math.ceil((v - fees[0])/fees[2])*fees[3]
        else:
            result = fees[1]
        
        answer.append(result)

    
    return answer