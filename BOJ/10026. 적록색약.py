import sys

sys.stdin = open('10026.txt', 'r')
from collections import deque
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def BFS(start_x, start_y, start_char):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()

        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > N - 1 or yy < 0 or yy > N -1 :
                continue
            if visited[xx][yy]:
                continue
            if start_char == data[xx][yy]:
                queue.append((xx, yy))
                visited[xx][yy] = 1

def BFS2(start_x, start_y, start_char):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 1
    if start_char == 'R' or start_char == 'G':
        while queue:
            x, y = queue.popleft()

            for a, b in direction:
                xx = x + a
                yy = y + b
                if xx < 0 or xx > N - 1 or yy < 0 or yy > N -1 :
                    continue
                if visited[xx][yy]:
                    continue
                if data[xx][yy] == 'R' or data[xx][yy] == 'G':
                    queue.append((xx, yy))
                    visited[xx][yy] = 1
    else:
        while queue:
            x, y = queue.popleft()
            for a, b in direction:
                xx = x + a
                yy = y + b
                if xx < 0 or xx > N - 1 or yy < 0 or yy > N -1 :
                    continue
                if visited[xx][yy]:
                    continue
                if start_char == data[xx][yy]:
                    queue.append((xx, yy))
                    visited[xx][yy] = 1
N = int(input())

data = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0
count_rg = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0: 
            BFS(i, j, data[i][j])
            count += 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS2(i, j, data[i][j])
            count_rg += 1


print(count , count_rg)