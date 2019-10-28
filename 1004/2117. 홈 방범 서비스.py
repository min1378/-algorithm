import sys
sys.stdin = open('2117.txt', 'r')

def isWall(x, y):
    if x < 0 or x > N -1 :
        return True
    if y < 0 or y > N - 1:
        return True
    return False
def count_people(x, y, K):
    ans = 0
    N = 2 * K - 1
    idx = N // 2 + x - (K - 1)
    for j in range(y - (K - 1), y + N - (K - 1)):
        if isWall(idx, j) == False:
            if data[idx][j]:
                ans += 1

    for i in range(1 , K):
        for j in range(y + i - (K-1), y + N - i - (K-1)):
            if isWall(idx - i, j) == False:
                if data[idx - i][j]:
                    ans += 1
            if isWall(idx + i, j) == False:
                if data[idx + i][j]:
                    ans += 1

    return ans
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if data[i][j]:
                count += 1
    end = 1
    for K in range(1, N ** 2):
        cost = K * K + (K - 1) * (K - 1)
        if cost > count * M:
            end = K - 1
            break
        elif cost == count * M:
            end = K
            break
    gain = 0
    answer = 0

    for K in range(1, end + 1):
        cost = K * K + (K - 1) * (K - 1)
        for i in range(N):
            for j in range(N):
                temp = count_people(i, j, K)
                if temp >= answer and temp * M >= cost:
                    answer = temp


    print("#{} {}".format(test_case,answer))