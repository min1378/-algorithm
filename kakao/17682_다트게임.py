def solution(dartResult):
    result = []
    temp = ""
    for char in dartResult:
        if char.isdigit():
            temp += char
        elif char.isalpha():
            if char == "S":
                result.append(int(temp))
            elif char == "D":
                result.append(int(temp) ** 2)
            elif char == "T":
                result.append(int(temp) ** 3)
            temp = ""
        else:

            if char == "*":
                if len(result) > 1:
                    result[-2] *= 2
                result[-1] *= 2
            elif char == "#":
                result[-1] *= -1


    answer = sum(result)
    return answer

solution("1S2D*3T")