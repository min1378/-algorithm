def solution(arr):
    answer = []
    check = -1
    for number in arr:
        if check == number:
            continue
        else:
            answer.append(number)
            check = number
    
    return answer