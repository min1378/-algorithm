import sys
sys.stdin = open('13460.txt', 'r')
TC = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def move(red, blue, mode, count):
    global min_count
    red_x = red[0]
    red_y = red[1]
    blue_x = blue[0]
    blue_y = blue[1]
    count += 1
    red_count = 0
    blue_count = 0
    flag_red = False

    # 파란색 움직임
    while True:
        blue_xx = blue_x + dx[mode]
        blue_yy = blue_y + dy[mode]
        blue_count += 1
        if [blue_xx, blue_yy] == out:
            return
        if data[blue_xx][blue_yy] == '#':
            new_blue = [blue_x, blue_y]
            blue_count -= 1
            break
        blue_x = blue_xx
        blue_y = blue_yy


    while True:
        red_xx = red_x + dx[mode]
        red_yy = red_y + dy[mode]
        red_count += 1
        if [red_xx, red_yy] == out:
            flag_red = True
            break

        if data[red_xx][red_yy] == '#':
            new_red = [red_x, red_y]
            red_count -= 1
            break

        red_x = red_xx
        red_y = red_yy


    if flag_red :
        if count < min_count:
            min_count = count
        return



    if new_red == new_blue:
        if red_count > blue_count:
            new_red[0] -= dx[mode]
            new_red[1] -= dy[mode]
        else:
            new_blue[0] -= dx[mode]
            new_blue[1] -= dy[mode]

    if red == new_red and blue == new_blue:
        return


    for mode2 in range(4):
        if (mode + mode2) % 2:
            queue.append([new_red, new_blue, mode2, count])


#for test_case in range(1, TC+1):
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
count = 0
min_count = 100
red_list = []
blue_list = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 'R':
            red = [i, j]
        elif data[i][j] == 'B':
            blue = [i, j]
        elif data[i][j] == 'O':
            out = [i, j]
queue = []
for mode in range(4):
    queue.append([red, blue, mode, count])

while queue:

    red, blue, mode, count = queue.pop(0)
    if count > 9 or count > min_count:
        continue
    move(red, blue, mode, count)

if min_count == 100:
    min_count = -1
print(min_count)



