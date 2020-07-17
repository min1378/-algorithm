def divider_list(n):
    if n == 1:
        return 1
    answer = []
    check = [0] * (n + 1)
    for divisor in range(1, n//2):
        if check[divisor] :
            continue
        remainder = n % divisor
        if remainder == 0:
            if divisor != n // divisor:
                check[divisor] = 1
                check[n // divisor] = 1
                answer.append(divisor)
                answer.append(n // divisor)
            else:
                check[divisor] = 1
                answer.append(divisor)
    if answer == []:
        answer.append(1)
        answer.append(n)
    return answer


def solution(n, m):
    answer = []
    n_list = divider_list(n)
    m_list = divider_list(m)
    Max = max([i for i in n_list if i in m_list])
    Min = Max * (n / Max) * (m / Max)
    answer = [Max, int(Min)]
    return answer   


print(solution(2, 5))