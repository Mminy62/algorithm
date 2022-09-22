def solution(id_list, report, k):
    answer = []
    
    #1. 신고당한 사람의 횟수만 알자 frodo 2번, neo 2번, Muzi 1번 => values로 알 수 있음
    #2. k이상 신고당한 사람의 이름 알기
    #3. 신고당한 사람 있으면 뱉기
    
    id_dict = {}
    
    for key in id_list:
         id_dict[key] = []
    
    for data in list(set(report)):
        key, value = data.split(' ')
        id_dict[key].append(value)
        
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
        
        
    # #2) unpacking 한 튜플로 신고당한 횟수 구함   
    # for data in temp: 
    #     if data in report_dict.keys():
    #         report_dict[data] += 1
    

#     id_dict = {}
#     report_dict = {}
#     report_name = []
    
    
#     report = list(set(report))
#     print(report)
    
#     for key in id_list:
#         id_dict[key] = None

#     for key in id_list:
#         report_dict[key] = 0
    
#     #유저가 신고한 아이디 정리
#     for data in report:
#         key, value = data.split(' ')
#         if not id_dict[key]: #None
#             id_dict[key] = [value]
#         else:
#             if value not in id_dict[key]:
#                 id_dict[key].append(value)
    
#     #신고한 아이디의 값을 통해 신고 당한 횟수 정리
#     #1) list unpacking
#     temp = ()
#     for row in list(id_dict.values()):
#         if row:
#             temp = temp + (*row,)
            
#     #2) unpacking 한 튜플로 신고당한 횟수 구함   
#     for data in temp: 
#         if data in report_dict.keys():
#             report_dict[data] += 1
    
#     #신고당한 사람 이름 알았음
#     for key, value in report_dict.items():
#         if value >= int(k):
#             report_name.append(key)

#     for data in id_dict.values():
#         if data is not None and report_name:
#             temp = list(set(report_name) - set(data))
#             answer.append(k - len(temp))
#         else:
#             answer.append(0)
    
    return answer