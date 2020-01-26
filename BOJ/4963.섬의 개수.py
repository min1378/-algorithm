import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

direction = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)]

def BFS(start_x, start_y):
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()

        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > H - 1 or yy < 0 or yy > W - 1:
                continue
            if visited[xx][yy]:
                continue
            if data[xx][yy]:
                queue.append((xx, yy))
                visited[xx][yy] = 1
        


while True:
    temp = input()
    W, H = map(int, temp.split())
    if W == 0 or H == 0:
        break
    count = 0
    data = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if visited[i][j] :
                continue
            if data[i][j]:
                BFS(i, j)
                count += 1
    
    print(count)