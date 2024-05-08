def solution(record):
    answer = []
    user = {}
    for sen in record:
        sen = sen.split()
        cmd = sen[0]
        if cmd == "Enter" or cmd == "Change":
            user[sen[1]] = sen[2]
    
    for sen in record:
        sen = sen.split()
        cmd = sen[0]
        result = ''
        if cmd == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(user[sen[1]]))
        if cmd == "Leave":
            answer.append("{0}님이 나갔습니다.".format(user[sen[1]]))
    
    return answer