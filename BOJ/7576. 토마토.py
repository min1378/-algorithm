import sys
sys.stdin = open('7576.txt', 'r')
#TC = 5
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1 :
        return True
    return False

def solve():
    global zero_count
    count = 0
    if zero_count == 0:
        return count
    while True:
        flag = True
        for _ in range(len(checks)):
            x, y = checks.popleft()
            for mode in range(4):
                xx = x + dx[mode]
                yy = y + dy[mode]
                if isWall(xx, yy):
                    continue
                if data[xx][yy] or data[xx][yy] == -1:
                    continue
                zero_count -= 1
                checks.append((xx, yy))
                data[xx][yy] = 1
                flag = False
        count += 1
        if zero_count == 0:
            return count

        if flag:
            return -1



#for test_case in range(1, TC+1):
M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
checks = deque([])
zero_count = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            checks.append((i, j))
        if data[i][j] == 0:
            zero_count += 1
print(solve())