import sys
sys.stdin = open('i1018.txt', 'r')
TC = 2
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def solve(start_x, start_y, character):
    x = start_x
    y = start_y
    check = character
    for a, b in direction:
        xx = x + a
        yy = y + b
        if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
            continue
        if visited[xx][yy]:
            continue
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    visited = [[0] * M for _ in range(N)]
    data = [list(input()) for _ in range(N)]
    if N % 2 :
        
    for i in range(N):
        for j in range(M):
            solve(i, j, data[i][j])