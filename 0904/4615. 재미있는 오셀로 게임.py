#import sys
from pprint import pprint
#sys.stdin = open('4615.txt', 'r')
# 벽체크 함수
def isWall(x, y):
    if x > N or x < 1 :
        return True
    if y > N or y < 1 :
        return True
    return False
# 색을 바꿔야할 돌의 위치 체크.
def enermy_check(x, y, mode, color):
    check_enermy = []
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    while True:
        # 전달받은 mode로 한 발자국 나아간다.
        test_x = x+dx[mode]
        test_y = y+dy[mode]
        # 벽이라면 그 전까지 체크한 위치는 무시하고 빈 리스트 []를 반환
        if isWall(test_x, test_y) == True:
            return []
        # 같은 색을 만났다면 그동안 체크한 좌표의 리스트를 반환
        if data[test_y-1][test_x-1] == color:
            return check_enermy
        # 0을 만났다면 비어 있는 공간이므로 빈리스트 [] 반환
        if data[test_y-1][test_x-1] == 0:
            return []
        # 나머지 조건들은 좌표를 체크하여 check_enermy에 저장한다.
        else :
            check_enermy.append([test_x, test_y])
            # 좌표를 체크하였다면 갱신시킨다.
            x = test_x
            y = test_y

# 검사하는 함수
def inspect(x, y, color):
    # 8방향 모드의 반복문을 실행한다.
    for mode in range(8):
        # enermy_check의 리턴 값을 받아온다.
        result = enermy_check(x, y, mode, color)
        # 만약 빈리스트가 아니라면
        if result != []:

            # result에서 좌표를 꺼내 data에 색칠한다.
            for check_x, check_y in result:
                data[check_y-1][check_x-1] = color


TC=int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    data = [[0]*N for _ in range(N)]
    # 흑은 1 백은 2
    data[N // 2 - 1][N // 2 - 1] = 2
    data[N // 2 - 1][N // 2] = 1
    data[N // 2][N // 2 - 1] = 1
    data[N // 2][N // 2] = 2


    check = [list(map(int, input().split())) for _ in range(M)]

    while True:


        if check == []:
            break

        #check에서 앞에서 하나씩 꺼내서 돌을 놓는다.
        x, y, color = check.pop(0)

        data[y-1][x-1] = color
        # 돌을 놓았을 때 어떻게 변화할 지 확인한다.
        inspect(x, y, color)

    # 반복문이 끝나면 모든 돌을 놓았다는 것이므로 흑돌과 백돌의 개수를 체크한다.
    black = 0
    white = 0
    for line in data:
        black += line.count(1)
        white += line.count(2)
    print("#{} {} {}".format(test_case, black, white))