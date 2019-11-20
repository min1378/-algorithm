def solution(progresses, speeds):
    answer = []

    N = len(speeds)
    temp = []
    count = 0
    check = 0
    for i in range(N):
        temp.append(round((100 - progresses[i]) / speeds[i]))
    while True:
        min = temp[0+count]
        for i in range(count, N):
            if N-count != 1:
                if min < temp[i]:
                    count = i
                    break
            else:
                count = 1
                break

        answer.append(count)
        check += count
        if check == N:
            break
    return answer

progresses = [1, 90, 97]
speeds = [1,30,5]
result=solution(progresses, speeds)
print(result)