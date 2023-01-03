def solution(arr):
    arr.remove(min(arr))
    if not len(arr):
        return [-1]
    return arr