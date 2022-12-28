def solution(a, b):
    answer = ''
    #윤년 -> 유일하게 2월에 2/29이 추가되어 1년이 366일이 되는 것을 의미한다. 
    #윤년의 조건 -> (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    #[날수를 이용하여 요일 구하기] https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=itinstructor&logNo=100201553237
    
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    date = sum(months[0:a-1]) + b
    
    answer = days[(date % 7)]
    
    return answer