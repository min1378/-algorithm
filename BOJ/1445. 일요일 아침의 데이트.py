import sys
sys.stdin = open('1445.txt', 'r')

def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, count, t, side_t):
    global trash
    global side_trash

    for mode in range(4):
        xx = x + dx[mode]
        yy = y + dy[mode]
        if isWall(xx, yy):
            continue
        if data[xx][yy] == 'F':
            if trash > t:
                trash = t
                side_trash = side_t
            return

        if data[xx][yy] == 'g':
            visited[xx][yy] = 1
            DFS(xx, yy, count+1, t, side_t)


        if data[xx][yy] == '.' and visited[xx][yy] == 0:
            visited[xx][yy] = 1
            temp_t = 0
            for mode2 in range(4):
                xxx = xx + dx[mode2]
                yyy = yy + dy[mode2]
                if isWall(xxx, yyy):
                    continue
                if data[xxx][yyy] == 'g':
                    temp_t += 1

            DFS(xx, yy, count + 1, t, side_t + temp_t)



N, M = map(int, input().strip().split())
data = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for line in data:
    print(line)
trash = N * M
side_trash = N * M
for i in range(N):
    for j in range(M):
        if data[i][j] == 'S':
            DFS(i, j, 0, 0, 0)
print(trash, side_trash)