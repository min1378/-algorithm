def solution(s):
    lower_s = s.lower()
    if lower_s.count("p") != lower_s.count("y"):
        return False
    return True

solution("pPoooyY")


def solution(s):
    count_p = 0
    count_y = 0
    for char in s:
        if char == "p" or char == "P":
            count_p += 1
        elif char == "y" or char == "Y":
            count_y += 1
        else:
            continue
    if count_p == count_y:
        return True
    return False