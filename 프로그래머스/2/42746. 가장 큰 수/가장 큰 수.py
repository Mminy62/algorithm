'''
완전탐색 X
문자열로 해서 앞자리가 큰 수대로 sorting
예외 케이스
3330 333의 경우 
333이 먼저 나와야함. -> 모든 숫자에 '0a'를 붙여서 정렬시켜보자
// 뒤에 문자만 붙이면 333a > 3335 가 되어버리므로, 다른 숫자를 배려해 뒤에 0을 붙인 후 문자를 붙이는 것
'''
def solution(numbers):
    # 1. 모든 수를 문자열로 변환
    numbers = list(map(str, numbers))

    # 2. 문자열을 4번 곱한 다음 원소의 값은 1000 이하이므로, [:4]로 해서 푸는 것
    # 그 정렬이 된 x를 sorting 하기
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    # 3. 정렬된 numbers를 이어붙인 뒤 반환
    answer = ''.join(numbers)
    

    return str(int(answer))