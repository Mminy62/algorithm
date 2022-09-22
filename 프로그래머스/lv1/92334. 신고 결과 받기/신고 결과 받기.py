def solution(id_list, report, k):
    answer = []
    
    #1. id_list를 기반으로 기본 dictionary key(신고한 사람), value(신고할 유저 id)생성
    #2. k이상 신고당한 사람의 이름 알기
    #3. 이름 기반으로 메일 보낼 횟수 count 
    
    id_dict = {}
    
    for key in id_list:
         id_dict[key] = []
    
    for data in list(set(report)):
        key, value = data.split(' ')
        id_dict[key].append(value)
    
    # unpacking 한 튜플로 신고당한 횟수 구함   
    temp = ()
    for row in list(id_dict.values()):
        if row:
            temp = temp + (*row,)
        
    report_name = []
    for name in id_list:
        if temp.count(name) >= int(k):
            report_name.append(name)
            
    for data in id_dict.values():
        count = 0
        if data: #data is not None
            for rn in report_name:
                if rn in data:
                    count += 1
                else:
                    count += 0
        answer.append(count)
    
    return answer
