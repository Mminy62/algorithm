from itertools import product
import heapq
def solution(users, emoticons):
    queue = []
    length_emoticon = len(emoticons)
    discount = [10, 20, 30, 40]
    
    for item_list in list(product(discount, repeat=length_emoticon)): # 순서 생각한 중복 순열
        # 이모티콘 할인율 리스트
        subscriber, price = 0, 0
        
        for (user_discount, user_price) in users:
            temp_price = 0
            discount_index = list(filter(lambda pi: item_list[pi] >= user_discount, range(length_emoticon)))
            for idx in discount_index:
                temp_price += emoticons[idx] * (100 - item_list[idx]) * 0.01
            
            if temp_price >= user_price:
                subscriber += 1
                
            else:
                price += temp_price
        
        heapq.heappush(queue, (-subscriber, -price))
            
    temp = list(heapq.heappop(queue))

    if temp[0] <= 0:
        temp[0] *= -1
    if temp[1] <= 0:
        temp[1] *= -1

    answer = temp
    return answer