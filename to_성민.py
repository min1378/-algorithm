import sys
sys.stdin = open("4615.txt", "r")

TC = int(input())

def isWall(x, y, chesspan_length):
    if x < 0 or x > chesspan_length - 1: return True
    if y < 0 or y > chesspan_length - 1: return True
    return False

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

for test_case in range(1, TC+1):
    chesspan_length, N = map(int, input().split())
    
    # 체스판 만들기
    chesspan = [[0] * chesspan_length for _ in range(chesspan_length)]
    chesspan[chesspan_length // 2][chesspan_length // 2] = chesspan[(chesspan_length // 2)-1][(chesspan_length // 2)-1] = 2
    chesspan[chesspan_length // 2][(chesspan_length // 2)-1] = chesspan[(chesspan_length // 2)-1][chesspan_length // 2] = 1


    for _ in range(N):
        x, y, color = list(map(int, input().split()))
        x -= 1
        y -= 1

        chesspan[y][x] = color

        if color == 1:
            t_color = 2
        elif color == 2:
            t_color = 1
        
        checks = []
        for diff in range(8):
            check = []
            new_x = x + dx[diff]
            new_y = y + dy[diff]
            while True:
                if isWall(new_x, new_y, chesspan_length) == True:
                    check = []
                    break
                if chesspan[new_y][new_x] == 0:
                    check = []
                    break
                if chesspan[new_y][new_x] == color:
                    break
                else:
                    check.append([new_y, new_x])
                    new_x = new_x + dx[diff]
                    new_y = new_y + dy[diff]
            checks.extend(check)

            # print(checks)
        # print(checks)
        for i in checks:
            chesspan[i[0]][i[1]] = color
        
        # 돌 색깔 세기
        black = 0
        white = 0
        for i in range(chesspan_length):
            for j in range(chesspan_length):
                if chesspan[i][j] == 1:
                    black += 1
                if chesspan[i][j] == 2:
                    white += 1

    print('#%s %s %s' % (test_case, black, white))
    
