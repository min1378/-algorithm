from collections import deque
TC = 8
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def spread(round):
    for _ in range(round):
        x, y, dust_amount = dust.pop()
        count = 0
        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > R - 1 or yy < 0 or yy > C - 1:
                continue
            if data[xx][yy] == -1:
                continue
            data[xx][yy] += dust_amount
            count += 1

        data[x][y] -= count * dust_amount

def move():
    # 위 라인
    up_dust = deque([])
    # 가로 넣기

    for i in range(C):

        up_dust.append(data[up_x][i])
    # 세로 넣기
    for i in range(up_x-1, -1, -1):

        up_dust.append(data[i][C-1])

    # 가로 넣기
    for i in range(C-2, -1, -1):

        up_dust.append(data[0][i])

    # 세로 넣기
    for i in range(1, up_x):

        up_dust.append(data[i][0])


    up_dust.rotate(1)
    up_dust[0] = -1
    up_dust[1] = 0

    for i in range(C):

        check = up_dust.popleft()
        data[up_x][i] = check
    for i in range(up_x-1, -1, -1):

        check = up_dust.popleft()
        data[i][C-1] = check
    for i in range(C-2, -1, -1):

        check = up_dust.popleft()
        data[0][i] = check
    for i in range(1, up_x):

        check = up_dust.popleft()
        data[i][0] = check


    # 아래 라인
    down_dust = deque([])
    for i in range(C):

        down_dust.append(data[down_x][i])

    for i in range(down_x+1, R):

        down_dust.append(data[i][C-1])

    for i in range(C - 2, -1, -1):

        down_dust.append(data[R-1][i])


    for i in range(R-2, down_x, -1):

        down_dust.append(data[i][0])


    down_dust.rotate(1)
    down_dust[0] = -1
    down_dust[1] = 0

    for i in range(C):
        check = down_dust.popleft()
        data[down_x][i] = check
    for i in range(down_x+1, R):
        check = down_dust.popleft()
        data[i][C-1] = check
    for i in range(C - 2, -1, -1):
        check = down_dust.popleft()
        data[R-1][i] = check
    for i in range(R-2, down_x, - 1):
        check = down_dust.popleft()
        data[i][0] = check


#for test_case in range(1, TC+1):
R, C, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]
air_machine = []
# 공기청정기 위치 저장
for i in range(R):
    if data[i][0] == -1:
        air_machine.append((i, 0))
        air_machine.append((i+1, 0))
        break
# 바람 라인 설정
up_x, up_y = air_machine[0]
down_x, down_y = air_machine[1]


for _ in range(T):
    dust = []
    for i in range(R):
        for j in range(C):
            if data[i][j] > 0:
                dust.append((i, j, data[i][j] // 5))

    spread(len(dust))
    move()
result = 0

for i in range(R):
    for j in range(C):
        if data[i][j] > 0:
            result += data[i][j]

print(result)