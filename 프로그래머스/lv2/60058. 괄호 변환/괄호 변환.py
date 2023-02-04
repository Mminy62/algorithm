def solution(p):
    answer = ''
    u, v = separate(p)

    # u, v로 분리시킨 다음 u가 올바른 것인지 검사해야함.
    # u 올바른지 검사
    # u 에 관련되어서만 처리하고 v는 마지막에 solution(v)로 처리한다. v(빈문자열) -> u가 되는 것까지
    if correct(u): #올바른 것
        answer += u
        if v:
            answer += solution(v)
    else:# 아닌 것
        answer += '('
        if v:
            answer += solution(v)
        answer += ')'
        # u 뒤바꾸기
        temp = ''
        u = list(u)
        u.pop(0)
        u.pop()
        for i in range(len(u)):
            if u[i] == '(':
                temp += ')'
            else:
                temp += '('
        answer += temp
    return answer

def separate(w):
    padict = {'(': 1, ')': -1}

    utemp = 0
    u = ''
    for pa in w:
        utemp += padict[pa]
        u += pa
        if utemp == 0:
            break

    v = w[len(u):]

    return (u, v)

def correct(u):
    stack = []
    top = ''
    for pa in list(u):
        stack.append(pa)
        if pa == ')' and len(stack) > 1:
            if top == '(':
                stack.pop()
                stack.pop()

        if stack:
            top = stack[-1]

    if not stack:
        return True
    else:
        return False
