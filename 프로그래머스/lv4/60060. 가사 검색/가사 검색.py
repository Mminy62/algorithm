from bisect import bisect_right, bisect_left

def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
        
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for keyword in queries:
        length = len(keyword)
        #keyword 별로 해당되는거 저장 나중에 count 하고 일단 temp
        cnt, left, right = 0, 0, 0

        if keyword[-1] == "?":
            left = bisect_left(array[length], keyword.replace("?", "a"))
            right = bisect_right(array[length], keyword.replace("?", "z"))

        else: # 접두사
            keyword = keyword[::-1]
            left = bisect_left(reversed_array[length], keyword.replace("?", "a"))
            right = bisect_right(reversed_array[length], keyword.replace("?", "z"))
            
        cnt = right - left
        answer.append(cnt)

    return answer
# from bisect import bisect_left, bisect_right


# def solution(words, queries):
#     answer = []
#     '''
#     풀이참조
#     접미사면 right를 찾을때 z로 대치
#     접두사면 시작부터 전부 다 찾기
#     '''

#     #길이를 기준으로 해본 다음에 효율성 낮으면 알파벳 기준으로 한번 더 이진탐색

#     array = [[] for _ in range(10001)]
#     reversed_array = [[] for _ in range(10001)]

#     for word in words:
#         array[len(word)].append(word)
#         reversed_array[len(word)].append(word[::-1])

#     for i in range(10001):
#         array[i].sort()
#         reversed_array[i].sort()

#     for query in queries:
#         count = 0
#         query_length = len(query)
#         array_length = len(array[query_length])
#         left = bisect_left(array[len(query)], query)

#         if query[-1] == "?":#접미사
#             left = bisect_left(array[len(query)], query.replace("?", "a"))
#             right = bisect_right(array[len(query)], query.replace("?", "z"))


#         else:#접두사인 경우 길이별로 순차 탐색
#             left = bisect_left(reversed_array[len(query)], query[::-1].replace("?", "a"))
#             right = bisect_right(reversed_array[len(query)], query[::-1].replace("?", "z"))


#         if left == right:
#             answer.append(0)
#         else:
#             count = right - left
#             answer.append(count)

#     return answer
