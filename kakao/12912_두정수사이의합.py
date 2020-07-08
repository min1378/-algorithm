# def solution(a, b):
#     answer = 0
#     start = min(a, b)
#     end = max(a, b)
#     if start == end:
#         answer = a
#         return answer
#     for number in range(start, end+1):
#         answer += number
#         print(answer)
    
#     return answer

def solution(a, b):
    answer = 0
    start = min(a, b)
    end = max(a, b)
    if start == end:
        answer = a
        return answer
    answer = sum(range(start, end+1))
    
    return answer
