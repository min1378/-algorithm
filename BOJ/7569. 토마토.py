import sys
#sys.stdin = open('7569.txt', 'r')
input = sys.stdin.readline
from collections import deque
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
direction = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
#TC = 3
#for test_case in range(1, TC+1):
count = 0
tomato = 0
M, N, H = map(int, input().split()) # 가로 세로 높이
data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
check_list = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if data[i][j][k] == 1 :
                tomato += 1
                check_list.append((i, j, k)) # 높이, 세로, 가로
            elif data[i][j][k] == -1:
                tomato += 1
while True:
    flag = False
    for _ in range(len(check_list)):
        x, y, z = check_list.popleft()

        for a, b, c in direction:
            xx = x + a
            yy = y + b
            zz = z + c
            if xx < 0 or xx > H - 1 or yy < 0 or yy > N - 1 or zz < 0 or zz > M - 1:
                continue
            if data[xx][yy][zz] == 0:
                flag = True
                data[xx][yy][zz] = 1
                tomato += 1
                check_list.append((xx, yy, zz))

    if flag == False:
        break
    count += 1

if tomato != N*M*H:
    count = -1

print(count)



