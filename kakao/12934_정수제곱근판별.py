def solution(n):
    answer = -1
    root_number = n ** 0.5
    list_number = list(str(root_number))
    # print(list_number)
    split_index = list_number.index(".") # 분리할 점 위치 찾기
    integer_list = list_number[:split_index] # 정수부분
    decimal_list = list_number[split_index + 1:] # 소수 부분
    if decimal_list[-1] == "0" and len(decimal_list) == 1:
        integer = int("".join(integer_list))
        answer = int((integer + 1) ** 2)
        return answer

    return answer

solution(9)
solution(10)

