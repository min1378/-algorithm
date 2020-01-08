import sys
from collections import deque
#sys.stdin = open('2178.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    return False


def solve(start_x, start_y):
    start_count = 1
    queue = deque([[start_x,start_y, start_count]])
    while True:
        x, y, count = queue.popleft()
        if x == N - 1 and y == M - 1 :
            return count
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy):
                continue
            if data[xx][yy] == '0':
                continue
            if visited[xx][yy] :
                continue
            queue.append([xx, yy, count+1])
            visited[xx][yy] = 1


N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(solve(0,0))