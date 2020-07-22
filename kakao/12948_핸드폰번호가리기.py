def solution(phone_number):
    answer = ''
    end = len(phone_number)
    temp = phone_number[end-4:end]
    answer = (end - 4) * "*" + temp
    return answer

