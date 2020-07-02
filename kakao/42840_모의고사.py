def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]


    for i in range(len(answers)):
        ans = answers[i]
        if ans == first[i % 5]:
            count[0] += 1
        if ans == second[i % 8]:
            count[1] += 1
        if ans == third[i % 10]:
            count[2] += 1
    maxCount = max(count)
    for i in range(len(count)):
        if count[i] == maxCount:
            answer.append(i+1)

    return answer