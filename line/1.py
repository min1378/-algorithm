def solution(inputString):
    check = [0] * 4
    answer = 0
    flag = True
    for el in inputString :
        if el == "(" :
            check[0] += 1
        elif el == ")" :
            if check[0] > 0:
                check[0] -= 1
                answer += 1
            else :
                flag = False
                break
        elif el == "{" :
            check[1] += 1
        elif el == "}" :
            if check[1] > 0:
                check[1] -= 1
                answer += 1
            else :
                flag = False
                break
        elif el == "[" :
            check[2] += 1
        elif el == "]" :
            if check[2] > 0:
                check[2] -= 1
                answer += 1
            else :
                flag = False
                break
        elif el == "<" :
            check[3] += 1
        elif el == ">" :
            if check[3] > 0:
                check[3] -= 1
                answer += 1
            else :
                flag = False
                break
    if flag == False:
        answer = -1
    elif sum(check) > 0:
        answer = -1
    
    return answer

print(solution("[line [plus]]"))
