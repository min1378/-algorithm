import sys
sys.stdin = open('1463.txt', 'r')

def DP(N):
    for i in range(2, N+1):




TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    dp = [100000] * (N+1)
    dp[1] = 1
    DP(N)
    print(dp[N])
    #print("#{} {}".format(test_case, dp[N]))

