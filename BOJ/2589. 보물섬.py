import sys
sys.stdin = open('2589.txt', 'r')
from collections import deque
def isWall(x, y):
    if x < 0 or x > N -1 or y < 0 or y > M - 1:
        return True
    return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x, y, count):

    max_count = 0
    q = deque()
    visited=[[False] * M for _ in range(N)]
    q.append([x, y, count])
    while q:
        x, y, count = q.popleft()
        if max_count < count :
            max_count = count

        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy): continue
            if visited[xx][yy] == False and data[xx][yy] == 'L':
                q.append([xx, yy, count + 1])
                visited[xx][yy] = True

    return max_count
N, M = map(int, (input().split()))
data = [list(input()) for _ in range(N)]
min_count = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 'L':
            count = BFS(i, j, 0)
            min_count = max(count, min_count)

print(min_count)