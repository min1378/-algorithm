#import sys
#sys.stdin = open('17143.txt', 'r')
#TC = int(input())



# 인덱스를 넘어가는지 확인하는 isWall
def isWall(x, y):
    if x < 0:
        return 1
    if x > R - 1:
        return 2
    if y < 0 :
        return 3
    if y > C - 1:
        return 4

    return False
# 고기를 잡자
def fishing(walk):
    sharks = []
    global result

    # 상어가 죽지 않았고 현재 위치에 상어가 있다면 다 넣는다.
    for i in range(M):
        if death_shark[i] == False:
            if shark_info[i][1] == walk:

                sharks.append(shark_info[i])

    #잡힌 상어가 없으면 끝냄
    if sharks == []:
        return

    # 최소거리에 있는 상어를 찾는다.
    min_range = sharks[0][0]
    check = sharks[0][5]
    for i in range(len(sharks)):
        if min_range > sharks[i][0]:
            min_range = sharks[i][0]
            check = sharks[i][5]

    # 최소거리에 있는 상어의 인덱스를 찾아 result에 크기를 더한다.
    for shark in sharks:
        if shark[5] == check:
            death_shark[shark[5]] = True
            data[shark[0]][shark[1]] -= 1
            result += shark[4]


# 상어끼리 공격
def attack(x, y, count):
    number = count
    sharks = []

    # 같은위치에 있는 상어를 찾는다.
    for i in range(M):
        if number == 0:
            break
        if death_shark[i] == False:
            if shark_info[i][0] == x and shark_info[i][1] == y:
                sharks.append(shark_info[i])
                number -= 1


    # 크기 최대값인 상어를 찾는다.
    max_size = sharks[0][4]
    check = sharks[0][5]

    for i in range(len(sharks)):
        if max_size < sharks[i][4]:
            max_size = sharks[i][4]
            check = sharks[i][5]


    # 크기가 작은 상어들을 다 죽인다.
    for shark in sharks:
        if shark[5] != check:
            death_shark[shark[5]] = True
            data[shark[0]][shark[1]] -= 1


# 상어들이 움직인다.
def move():
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]
    for i in range(M):
        # 상어가 죽지 않았다면 이동한다.
        if death_shark[i] == False:
            x = shark_info[i][0]
            y = shark_info[i][1]
            s = shark_info[i][2]
            mode = shark_info[i][3]
            data[x][y] -= 1
            count = max(abs(dx[mode]*s), abs(dy[mode]*s))
            for _ in range(count):
                Test_X = x + dx[mode]
                Test_Y = y + dy[mode]


                # 벽에 부딪혔을 때 방향을 바꿔준다.
                if isWall(Test_X, Test_Y) == 1:
                    Test_X = 1
                    mode = 2

                elif isWall(Test_X, Test_Y) == 2:
                    Test_X = R - 2
                    mode = 1

                elif isWall(Test_X, Test_Y) == 3:
                    Test_Y = 1
                    mode = 3

                elif isWall(Test_X, Test_Y) == 4:
                    Test_Y = C - 2
                    mode = 4

                x = Test_X
                y = Test_Y
            shark_info[i][0] = x
            shark_info[i][1] = y
            shark_info[i][3] = mode

            data[x][y] += 1

#for test_case in range(1, TC+1):
R, C, M = map(int, input().split())
shark_info = [list(map(int, input().split())) for _ in range(M)]
data = [[0 for _ in range(C)] for _ in range(R)]




for i in range(M):
    # 인덱스를 붙여준다.
    shark_info[i] += [i]
    # 좌표 영점 맞춘다.
    shark_info[i][0] -= 1
    shark_info[i][1] -= 1
    # 상어 위치 맵에 체크
    data[shark_info[i][0]][shark_info[i][1]] += 1

death_shark = [False] * M
result = 0
for walk in range(C):

    fishing(walk)

    move()

    #위치 맵을 돌아 두마리 이상일때 싸움을 시작한다.
    for i in range(R):
        for j in range(C):
            if data[i][j] > 1:
                attack(i, j, data[i][j])

print(result)
