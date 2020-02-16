import sys
sys.stdin = open('i14500.txt', 'r')
from copy import deepcopy
direction = [(-1, 0), (0, 1), (1, 0)]
direction2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def DFS(x, y, result, list):
    global max_result
    if visited[x][y]:
        return
    if max_result - result >= 1000 * ( 4-len(list) ):
        return
    if len(list) == 4:
        print(list)
        max_result = max(max_result, result)
        return
    visited[x][y] = 1
    if len(list) == 3:
        x, y = list[1]
        for a, b in direction2:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
                continue
            DFS(xx, yy, result + data[xx][yy], list + [(xx, yy)])

    for a, b in direction:
        xx = x + a
        yy = y + b
        if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
            continue

        DFS(xx, yy, result + data[xx][yy], list + [(xx, yy)])
    visited[x][y] = 0

    
    
    

TC = 22
#for test_case in range(1, TC+1):
max_result = 0
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        for line in visited:
            print(line)
        DFS(i, j, data[i][j], [(i, j)])
print(max_result)
