import sys
#sys.stdin = open('1012.txt', 'r')
input = sys.stdin.readline
from collections import deque
TC = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    return False

def BFS(start_x, start_y):
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()

        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy):
                continue
            if visited[xx][yy]:
                continue
            if data[xx][yy] :
                visited[xx][yy] = 1
                queue.append((xx, yy))





for test_case in range(1, TC+1):
    M, N, K = map(int, input().split())
    data = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        data[y][x] = 1
    visited = [[0] * M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if data[i][j]:
                BFS(i, j)
                count +=1


    print(count)