def solution(day, k):
    first_day = day
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = []
    diff = k-1
    for days in days_month:
        if ((first_day + diff)% 7 == 5 or (first_day + diff)% 7 == 6):
            answer.append(1)
        else:
            answer.append(0)
        first_day = (first_day + days) % 7
    
    return answer


print(solution(6, 1))