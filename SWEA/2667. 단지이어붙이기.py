import sys
sys.stdin = open('2667.txt', 'r')
def isWall(x, y):
    if x < 0 or x > N - 1:
        return True
    if y < 0 or y > N - 1:
        return True
    return False
def DFS(i, j):
    global union_number
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = [[i, j]]
    count = 0
    while stack:

        x, y = stack.pop()
        if data_map[x][y] :
            data_map[x][y] = 0
            count += 1
            for mode in range(4):
                Test_X = x + dx[mode]
                Test_Y = y + dy[mode]
                if isWall(Test_X, Test_Y) == False and data_map[Test_X][Test_Y] == 1:
                        stack.append([Test_X, Test_Y])


    union_number += 1
    return count

N = int(input())
data_map =[list(map(int, input())) for _ in range(N)]
union_number = 0
home_count = []
for i in range(N):
    for j in range(N):
        if data_map[i][j] == 1:

            temp = DFS(i,j)
            home_count.append(temp)

print(union_number)
home_count.sort()
for number in home_count:
    print(number)

