import sys
sys.stdin = open('1463.txt', 'r')

def DP(N):
    for i in range(2, N+1):
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        if i - 1 != 0:
            dp[i] = min(dp[i], dp[i-1] + 1)



#TC = int(input())
#for test_case in range(1, TC+1):
N = int(input())
dp = [100000] * (N+1)
dp[1] = 0
DP(N)
print(dp[N])
    #print("#{} {}".format(test_case, dp[N]))

