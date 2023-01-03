def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
#print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
# def solution(s, n):
#     answer = []
    
#     for c in list(s):
#         if c.isalpha():
#             temp = ord(c) + n
    
#             if c.islower() and temp > 122 or c.isupper() and temp > 90:
#                 temp -= 26
            
#             answer.append(chr(temp))
#         else:
#             answer.append(c)
                
#     return ''.join(answer)