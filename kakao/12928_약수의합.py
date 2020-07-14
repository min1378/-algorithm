def solution(n):
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
    return sum(answer)

print(solution(1))
print(solution(9))