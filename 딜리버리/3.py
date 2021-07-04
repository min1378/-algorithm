def solution(N):
    dp = [0 for i in range(N)]
    dp[0] = 0
    dp[1] = 1
    number = N
    for i in range(3, N + 1, 2):
        if (dp[1] + i < N):
            dp[dp[1] + i] = dp[1] + 1
    print(dp)
    print(dp)
    return [0]


print(solution(11))