import sys
sys.stdin = open('2636.txt', 'r')

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    return False


def BFS(x, y):
    q = deque([])
    q.append((x, y))
    data[x][y] = 2

    while q :
        x, y = q.popleft()

        for mode in range(4):
            testX = x + dx[mode]
            testY = y + dy[mode]
            if isWall(testX,testY) :
                continue

            if data[testX][testY] == 0 :
                data[testX][testY] = 2
                q.append((testX, testY))

def BFS2(x, y):
    q = deque([])
    q.append((x, y))
    data[x][y] = 3

    while q :
        x, y = q.popleft()

        for mode in range(4):
            testX = x + dx[mode]
            testY = y + dy[mode]
            if isWall(testX,testY) :
                continue

            if data[testX][testY] == 1 :
                data[testX][testY] = 4
                if data[testX+1][testY] == 2 or data[testX - 1][testY] == 2 or data[testX][testY + 1] == 2 or data[testX][testY - 1] == 2:
                    data[testX][testY] = 3
                q.append((testX, testY))

def cal():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                data[i][j] = 0
            elif data[i][j] == 3:
                data[i][j] = 0
                cnt += 1
            elif data[i][j] == 4:
                data[i][j] = 1
    return cnt


N,M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]



count = 0
while sum(sum(data, [])):
    count += 1
    BFS(0, 0)
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                BFS2(i, j)
    print("============")
    for line in data:
        print(line)
    last_cheeze = cal()
    print("============")
    for line in data:
        print(line)
print(count)
print(last_cheeze)