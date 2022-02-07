import sys

num = int(sys.stdin.readline())
room_height = 0
roon_width = 0


for i in range(num):
    h, w, n = map(int,sys.stdin.readline().rstrip().split(' '))

    if n % h == 0:
        room_width = n // h * 1
        room_height = h

    else:
        room_width = n // h + 1
        room_height = n % h

    if len(str(room_width)) < 2:
        print(str(room_height) + str(0) + str(room_width))
    else:
         print(str(room_height) + str(room_width))
        
 '''
 방번호 표현을 위해 출력에 0을 더했지만
 연산으로 room_height * 100 + room_width 를 출력하는 방식도 있음.
 
 '''
