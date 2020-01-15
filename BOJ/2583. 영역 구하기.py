import sys
sys.stdin = open('2583.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]
def isWall(x, y):
    if x < 0 or x > M - 1 or y < 0 or y > N - 1:
        return True
    return False

def DFS(start_x, start_y):
    area = 1
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = 1
    while stack:
        x, y = stack.pop()
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy):
                continue
            if visited[xx][yy]:
                continue
            if data[xx][yy] == 0:
                visited[xx][yy] = 1
                stack.append((xx, yy))
                area += 1

    return area
M, N, K = map(int, input().split())
data = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
count = 0
for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())
    diff_x = end_x - start_x
    diff_y = end_y - start_y

    for i in range(start_x, end_x):

        for j in range(start_y, end_y):

            data[j][i] = 1

result = []
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        if data[i][j] == 0:
            result.append(DFS(i, j))
            count += 1
result.sort()
print(count)
print(' '.join(map(str, result)))