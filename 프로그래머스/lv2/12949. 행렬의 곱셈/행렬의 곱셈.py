def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    # A의 열의 수 = B의 행의 수(i -> j, j는 그대로 행만 바뀜)
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp = 0
            for c in range(len(arr1[i])):#i행의 열의 개수
                temp += arr1[i][c] * arr2[c][j]
            answer[i][j] = temp
                
    
    return answer