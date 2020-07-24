def solution(dartResult):
    result = [] # 담는 칸
    temp = "" # 엘레먼트

    for char in dartResult:
        print(char) # 1 0 S 
        if char.isdigit(): # 숫자일때
            temp += char # 1 10

        elif char.isalpha(): # 보너스일때
            if char == "S":
                result.append(int(temp)) # result = [10]
            elif char == "D":
                result.append(int(temp) ** 2)
            elif char == "T":
                result.append(int(temp) ** 3)
            temp = ""

        else: # 옵션일때
            if char == "*":
                if len(result) > 1:
                    result[-2] *= 2 
                result[-1] *= 2 
            elif char == "#":
                result[-1] *= -1
            

    answer = sum(result)
    return answer

solution("10S")