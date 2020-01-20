import sys
#sys.stdin = open('2206.txt', 'r')
from collections import deque

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def BFS():
    queue = deque([(0, 0, 0, 1)])
    visited[0][0][0] = 1
    while queue:

        x, y, check, count = queue.popleft()
        if x == N - 1 and y == M - 1:
            return count
        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
                continue


            if visited[xx][yy][check]:
                continue
            if check == 1:
                if data[xx][yy]:
                    continue
                else:
                    queue.append((xx, yy, 1, count + 1))
                    visited[xx][yy][1] = 1
            elif check == 0:
                if data[xx][yy]:
                    queue.append((xx, yy, 1, count + 1))
                    visited[xx][yy][1] = 1
                else:
                    queue.append((xx, yy, 0, count + 1))
                    visited[xx][yy][0] = 1

    return -1
TC = 1
#for test_case in range(1, TC+1):
N, M = map(int, input().split())
visited = [[[0 for depth in range(2)] for col in range(M)] for row in range(N)]

data = [list(map(int, input())) for _ in range(N)]
print(BFS())
        