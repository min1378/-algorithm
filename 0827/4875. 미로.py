import sys
sys.stdin = open('4875.txt', 'r')

TC = int(input())


# 벽을 검증하는 함수!
def isWall(x, y, N):
    if x < 0 or x >= N: return True
    if y < 0 or y >= N: return True
    return False

for test_case in range(1, TC+1):
    N = int(input())
    # 맵데이터 행렬
    data = [[0] * N for i in range(N)]
    # 방문했는지 여부 확인
    visited = [[False] * N for i in range(N)]
    # 방향 0(위) 1(오른쪽) 2(아래) 3(왼쪽) 시계방향!
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    stack = []

    # 데이터값 입력받기
    for i in range(N):
        row = list(map(str, input()))
        data[i] = list(map(int, row))

    # 시작위치 찾기.
    for i in range(N) :
        for j in range(N):
            if data[i][j] == 2:
                x = i
                y = j
                break

    #이동하는 무한루프
    while True:
        # 출구인 3을 찾았을때 종료.
        if data[x][y] == 3:
            result = 1
            break

        # 4방향으로 움직이는 포문.
        for mode in range(4):
            testX = x + dx[mode]
            testY = y + dy[mode]
            # 4방향으로 한칸 움직였을때, 벽이 아니고 방문하지 않은 지역이면 stack에 추가.
            if isWall(testX,testY,N-1) == False and visited[testX][testY] == False and data[testX][testY] == 0:
                stack.append([testX, testY])

        # stack이 비어있다면 출구에 도달할 수 없는 경로이기 때문에 종료.
        if stack == [] :
            result = 0
            break

        # 현재 위치를 방문했다고 기록
        visited[x][y] = True

        # 다음위치를 stack에서 꺼내 갱신한다.
        temp = stack.pop()
        x = temp[0]
        y = temp[1]

    print("#{} {}".format(test_case, result))








