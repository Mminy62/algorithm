def check(answer):
    # 기둥과 보의 좌표를 보고 해당 기준에 성립하는지 -> 아닌게 나오면 좌표, 맞으면 0
    # 기둥이라면
    for x, y, stuff in answer:
        if stuff == 0:
            # 바닥 위에 / 보의 한쪽 끝에 / 또 다른 기둥 위에
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else: # 아닌 경우
                return False

        # 보 라면
        if stuff == 1:
            # 양쪽 끝이 다른 보와 동시에 연결 / 한쪽 끝이 기둥 위
            if ([x-1, y, 1] in answer and [x+1, y, 1] in answer) or [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            else:
                return False

    return True

def solution(n, build_frame):
    answer = []
    # 설치할거면 해당 좌표만 확인
    # 삭제할거면 전체 gidung, bo 확인
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 1:# 설치
            # 일단 설치 해보고 아니면 제거
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])

        if b == 0:# 삭제
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    return sorted(answer)