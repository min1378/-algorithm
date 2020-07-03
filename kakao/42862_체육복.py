def solution(n, lost, reserve):
    answer = 0
    length = len(lost)
    for _ in range(length):
        lost_person = lost.pop(0)
        if lost_person in reserve:
            idx = reserve.index(lost_person)
            reserve.pop(idx)
        else :
            lost.append(lost_person)
    length = len(lost)
    for _ in range(length):
        lost_person = lost.pop(0)
        if lost_person - 1 in reserve:
            idx = reserve.index(lost_person - 1)
            reserve.pop(idx)
        elif lost_person + 1 in reserve:
            idx = reserve.index(lost_person + 1)
            reserve.pop(idx)
        else:
            lost.append(lost_person)
    answer = n - len(lost)
    return answer

print(solution(5, [2,4], [3,5]))