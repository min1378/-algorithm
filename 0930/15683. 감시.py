import sys
sys.stdin = open('15683.txt', 'r')
TC = int(input())
def isWall(x, y):
    if x < 0 or x > M-1:
        return True
    if y < 0 or y > N-1:
        return True
    return False

def DFS(x, y, mode):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 0
    while True:
        x = x + dx[mode]
        y = y + dy[mode]
        if isWall(x,y) or data[x][y] == 6:
            return count
        elif 0 < data[x][y] < 6 or data[x][y] == '#':
            continue
        data[x][y] = '#'
        count += 1
    return count
def solve(cctvs, count):
    for i in range(len(cctvs)):
         if cctvs[i]


for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    cctvs = []
    for i in range(N):
        for j in range(M):
            if 0 < data[i][j] < 6:
                cctvs.append([data[i][j], [i,j]])

    sight = {
        1 : [[0], [1], [2], [3]],
        2 : [[1, 3], [0, 2]],
        3 : [[0, 1], [0, 3], [2, 3], [1, 2]],
        4 : [[0, 1, 3], [1, 2, 3]],
        5 : [0, 1, 2, 3]
    }
    print(sight)
    print(cctvs)
    # solve(cctvs, 0)

