def solution(n):
    answer = 0
    is_prime = [False, False] + [True] * (n - 1)
    primes = []
    # print(is_prime)
    for number in range(2, n + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple_prime in range(2 * number, n + 1, number): # 4 6 8 10 
                is_prime[multiple_prime] = False
    # print(prime)
    return len(primes)

