def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    min_number = min(arr)
    min_index = arr.index(min_number)
    arr.pop(min_index)
    answer = arr
    return answer