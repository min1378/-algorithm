def solution(a, b):
    answer = ''
    days = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day_to_number =[0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    
    day_number = day_to_number[a - 1] + b
    answer = days[day_number % 7]
    return answer

print(solution(5, 24))