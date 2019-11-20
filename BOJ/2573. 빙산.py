import sys
sys.stdin = open('2573.txt', 'r')
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    return False
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(i, j):
    s = []
    s.append([i, j])
    visited[i][j] = True
    while s:

        x, y = s.pop()
        count = 0
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]

            if isWall(xx, yy): continue
            if data[xx][yy] == 0:
                count += 1
        if data[x][y] <= count:
            data[x][y] = -1
        else:
            data[x][y] -= count

        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if visited[xx][yy] == False and data[xx][yy] > 0:
                s.append([xx, yy])
                visited[xx][yy] = True






N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
count = 0
year = 0
while True:
    year += 1
    visited = [[False] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and data[i][j] > 0:
                count += 1
                DFS(i, j)


    for i in range(N):
        for j in range(M):
            if data[i][j] == -1: data[i][j] = 0

    if count > 1:
        year -= 1
        break
    if count == 0:
        year = 0
        break

print(year)