def solution(s):
    answer = ''
    sen = s.replace(' ', '+=')
    print(sen)
    cases = sen.split('+')
    print(cases)
    for word in cases:
        if word == '=':
            answer += ' '
        elif word[0] == '=':
            answer += ' ' + word[1:].capitalize()
        else:
            answer += word.capitalize()
        
    return answer