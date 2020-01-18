import sys
#sys.stdin = open('7562.txt', 'r')
input = sys.stdin.readline
from collections import deque
TC = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
direction = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
def BFS(start_x, start_y):
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = 1
    while queue:
        x, y, count = queue.popleft()
        if x == end_x and y == end_y:
            return count
        for a, b in direction:
            xx = x + a
            yy = y + b

            if xx < 0 or xx > I - 1 or yy < 0 or yy > I - 1:
                continue
            if visited[xx][yy]:
                continue
            queue.append((xx, yy, count + 1))
            visited[xx][yy] = 1

for test_case in range(1, TC+1):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    data = [[0] * I for _ in range(I)]
    visited = [[0] * I for _ in range(I)]

    print(BFS(start_x, start_y))
