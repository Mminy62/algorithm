def solution(s):
    answer = ''

    array = list(map(int, s.split()))
    array.sort()
    answer += str(array[0])
    answer += ' ' + str(array[-1])
    
    return answer