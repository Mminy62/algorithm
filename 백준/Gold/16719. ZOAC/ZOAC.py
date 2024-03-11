arr = list(input().rstrip())

result = [""] * len(arr)

def solution(start, arr):
    if not arr:
        return

    min_value = min(arr)
    temp = arr.index(min_value)
    result[start + temp] = min_value
    print(''.join(result))
    solution(start + temp + 1, arr[temp + 1:])
    solution(start, arr[:temp])

solution(0, arr)