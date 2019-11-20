# import sys
# sys.stdin = open('17070.txt', 'r')
# TC = int(input())

def cal(x, y, state):
    result = 0
    if x == N-1 and y == N-1:
        return 1
    for mode in range(3):
        if (mode == 0 and state == 2) or (mode == 2 and state == 0):
            continue
        Test_X = x + dx[mode]
        Test_Y = y + dy[mode]
        if Test_X > N - 1 or Test_Y > N - 1 or data[Test_X][Test_Y] == 1:
            continue
        if mode == 1 and (data[x][y + 1] or data[x + 1][y]):
            continue
        result += cal(Test_X, Test_Y, mode)
    return result
#for test_case in range(1, TC+1):
dx = [0, 1, 1]
dy = [1, 1, 0]
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
print(cal(0, 1, 0))
