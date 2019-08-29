import sys
sys.stdin = open('5105.txt', 'r')

TC = int(input())
def isWall(x, y, N):
    if x > N-1 or x < 0 or y > N-1 or y < 0 :
        return True


    return False

for test_case in range(1, TC+1):
    N = int(input())
    data = []
    for i in range(N):
        temp = list(map(str, input()))
        data.append(list(map(int, temp)))
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x = i
                y = j
                break
    count = 0
    stack = []
    visited = [[False] * N for i in range(N)]

    while True :

        if data[x][y] == 3:
            break

        count += 1

        # append 되는 친구가 있나 확인하는 변수
        cnt = 0
        for mode in range(4):
            test_x = x + dx[mode]
            test_y = y + dy[mode]
            if isWall(test_x, test_y, N) == False and visited[test_x][test_y] == False:
                if data[test_x][test_y] != 1: # != 0 이라 append 안됨
                    stack.append([test_x, test_y, count])
                    cnt += 1

        # append 된 것도 없고 stack도 비어있으면 갈 곳 없음 => 0 으로 탈출
        if cnt == 0 and stack == []:
            count = 1
            break

        visited[x][y] = True

        if stack != []:
            x, y, count = stack.pop(0)


    print("#{} {}".format(test_case, count-1))