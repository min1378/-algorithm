import sys
sys.stdin = open('14499.txt', 'r')
TC = int(input())

# 방향 1, 2, 3, 4 => 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
def isWall(x, y):
    if x < 0 or y < 0 or x > N - 1 or y > M - 1:
        return True
    return False

def check(dir):
    xx = x + dx[dir]
    yy = y + dy[dir]
    if isWall(xx, yy):
        return
    dice[]


for test_case in range(1, TC+1):
    dice = [[0, 0, 0, 0], [0, 0, 0]]
    N, M, x, y, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    mode = 0
    print(data)
    command = list(map(int, input().split()))
    for i in command:
        if i == 1 or i == 2:
            mode = (mode + 1) % 2
        check(i)