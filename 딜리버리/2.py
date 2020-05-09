def sign(code, stack):
    if len(stack) < 2:
        return False
    else:
        first = stack.pop()
        second = stack.pop()

        if code == "+":
            new_number = first + second
            if new_number > 2**20 - 1:
                return False
        elif code == "-":
            new_number = first - second
            if new_number < -(2**20) - 1:
                return False
        stack.append(new_number)
    return True


def solution(S):
    # write your code in Python 3.6
    stack = []
    splited_codes = S.split(" ")
    for code in splited_codes:
        if code == "":
            continue
        elif code.isdigit():
            stack.append(int(code))
        elif code == "DUP":
            if len(stack) == 0:
                return -1
            else:
                new_number = stack[-1]
                stack.append(new_number)
        elif code == "POP":
            if len(stack) == 0:
                return -1
            else:
                stack.pop()
        else:
            if len(code) > 1:
                for symbol in code:
                    if symbol.isdigit():
                        stack.append(int(symbol))
                    else:
                        flag = sign(symbol, stack)
                        if flag is False:
                            return -1
            else:
                flag = sign(code, stack)
                if flag is False:
                    return -1
    if len(stack) == 0:
        return -1

    return stack[-1]


print(solution("13 DUP 4 POP 5 DUP + DUP + -"))