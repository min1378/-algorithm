def solution(array, commands):
    answer = []
    for command in commands:
        start, end, index = command
        
        new_array = array[start - 1:end]
        new_array.sort()
        answer.append(new_array[index - 1])


    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))