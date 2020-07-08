def solution(s):
    answer = True
    length = len(s)
    # check = "123456789"
    # for i in check:
    #     print(i, ord(i))
    if (length != 4 and length != 6):
        return False

    for char in s:
        if ord(char) < 48 or ord(char) > 57:
            return False
    return answer

print(solution("12345s"))
