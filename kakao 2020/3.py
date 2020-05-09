from collections import Counter



def solution(gems):
    result = set(gems)
    start = 0
    end = 1
    temp = set(gems[:end])
    length = len(gems)
    answer = []
    diff = 9999999
    while start < len(gems):
        if temp == result:
            answer_diff = abs(start+1 - end)
            if diff > answer_diff:
                diff = answer_diff
                answer = [start+1, end]
            elif diff == answer_diff:
                if answer[0] > start + 1:
                    answer = [start+1, end]
            start += 1
            temp = set(gems[start:end])
        else :
            if end != len(gems):
                end = length + 1
            else:
                start += 1
            if start == 0:
                temp = set(gems[:end])
            else:
                temp = set(gems[start:end])

    return answer


print(solution(	["AA", "AB", "AC", "AA", "AC"]))