def solution(arr, divisor):
    answer = []
    for number in arr:
        if number % divisor:
            continue
        else:
            answer.append(number)
    answer.sort()
    if answer == []:
        answer.append(-1)
    return answer