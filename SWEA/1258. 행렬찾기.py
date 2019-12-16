import sys
sys.stdin = open('1258.txt', 'r')
def isWall(x, y):
    global N
    if x> N-1 or x < 0 : return True
    if y > N-1 or y < 0 : return True

    return False

def checkEdge(x, y):
    global N

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    mode = 1
    while True:
        test_x = x+dx[mode]
        test_y = y+dy[mode]
        if isWall(test_x,test_y) == False and visited[test_y][test_x] == False and data[test_y][test_x]:
            x = test_x
            y = test_y
        elif mode == 1 and (isWall(test_x,test_y) == True or data[test_y][test_x] == 0):
            mode = 2

        elif mode == 2 and (isWall(test_x,test_y) == True or data[test_y][test_x] == 0):
            return [x, y]
TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]



    visited = [[0] * (N) for _ in range(N)]



    size = []
    while True:
        start_x = -1
        start_y = -1

        for i in range(N):
            flag = False
            for j in range(N):
                if visited[i][j] == 0 and data[i][j]:
                    start_y = i
                    start_x = j
                    flag = True
                    break

            if flag == True:
                break

        if start_x == -1 or start_y == -1 :
            break

        if data[start_y][start_x] and visited[start_y][start_x] == False:
            end_x, end_y = checkEdge(start_x, start_y)

            size.append([end_y-start_y+1, end_x -start_x+1])
            for i in range(start_y, end_y+1):
                for j in range(start_x, end_x+1):
                    visited[i][j] = 1


    N = len(size)
    result = ''



    for si in size:
        si.insert(0, si[0] * si[1])

    result_list = sorted(size)
    result += str(N) + ' '
    for i in range(N):
        result += str(result_list[i][1]) + ' ' + str(result_list[i][2]) + ' '

    print("#{} {}".format(test_case, result))
