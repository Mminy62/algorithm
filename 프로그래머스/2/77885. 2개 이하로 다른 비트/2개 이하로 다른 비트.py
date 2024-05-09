def solution(numbers):
    answer = []
    for num in numbers:
        tmp = list(bin(num)[2:])
        
        post = ''.join(tmp[-2:])
        if post == '11':
            tmp = ['0'] + tmp
            for i in range(len(tmp)-1, -1, -1):
                if tmp[i] == '0':
                    tmp = tmp[0:i] + ['1', '0'] + tmp[i+2:]
                    break

        else:# '01' or '00' or '10'
            tmp = list(bin(num + 1)[2:])

        answer.append(int(''.join(tmp), 2))
                    
    return answer