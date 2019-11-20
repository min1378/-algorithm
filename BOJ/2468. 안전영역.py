import sys
from copy import deepcopy
sys.stdin = open('2468.txt', 'r')
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > N -1 :
        return True
    return False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, height):
    s = []
    s.append([x, y])
    visited[x][y] = True
    while s:
        x, y = s.pop()
        for mode in range(4):
            Testx = x + dx[mode]
            Testy = y + dy[mode]
            if isWall(Testx, Testy) :
                continue
            if data[Testx][Testy] > height and visited[Testx][Testy] == False:
                s.append([Testx, Testy])
                visited[Testx][Testy] = True




N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_height = max(sum(data, []))

max_union_count = 1
for k in range(1, max_height):

    visited = [[False] * N for _ in range(N)]
    union_count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and data[i][j] > k:
                union_count += 1
                DFS(i, j, k)

    max_union_count = max(max_union_count, union_count)

print(max_union_count)



