def solution(s):
    answer = 0
    
    num_dict = {'zero': '0', 'one':'1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
               'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    
    enword = list(num_dict.keys())
    
    for k in enword:
        if k in s :
            s = s.replace(k, str(num_dict[k]))
    
    answer = int(s)
    
    return answer