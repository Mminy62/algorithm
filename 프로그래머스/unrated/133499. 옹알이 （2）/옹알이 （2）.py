def solution(babbling):
    answer = 0
    candi = ["aya", "ye", "woo", "ma"]
    before = 0
    
    for string in babbling:
        string = string.replace("aya","1").replace("ye", "2").replace("woo", "3").replace("ma", "4")

        if string.isnumeric():
            prev = None
            temp = 0
            for i in range(len(string)):
                if prev != string[i]:
                    prev = string[i]
                    temp += 1
                if temp == len(string):
                    answer += 1
    
    return answer