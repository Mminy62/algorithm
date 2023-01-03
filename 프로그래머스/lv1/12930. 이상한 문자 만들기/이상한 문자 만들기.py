def solution(s):
    answer = []
    sen = s.split(' ')
    
    for word in sen:
        word = list(word)
        for i, v in enumerate(word):
            if i % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
        answer.append(''.join(word))
        answer.append(' ')
        
        
    return ''.join(answer[:len(answer)-1])