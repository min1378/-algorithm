def isWall(x, y):
    if x < 0 or x > N - 1:
        return True
    if y < 0 or y > N - 1:
        return True
    return False
def DFS(x, y):
    open_kingdom[x][y] = union_number
    stack = []
    while True:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for mode in range(4):
            test_x = x + dx[mode]
            test_y = y + dy[mode]
            if isWall(test_x, test_y) == False:
                if open_kingdom[test_x][test_y] == -1 and abs(mapdata[test_x][test_y] - mapdata[x][y]) >= L and abs(
                        mapdata[test_x][test_y] - mapdata[x][y]) <= R:
                    open_kingdom[test_x][test_y] = union_number
                    stack.append([test_x, test_y])

        if stack == []:
            return

        x, y = stack.pop()

# TC = int(input())
# for test_case in range(1, TC+1):
N, L, R = map(int, input().strip().split())
mapdata = [list(map(int, input().strip().split())) for _ in range(N)]

count = 0
while True:
    open_kingdom = [[-1] * N for _ in range(N)]
    union_number = 0
    for i in range(N):
        for j in range(N):
            if open_kingdom[i][j] == -1:
                DFS(i, j)
                union_number += 1

    if union_number == N * N:
        break
    union_info = [[0, 0] for _ in range(union_number)]

    for i in range(N):
        for j in range(N):
            union_info[open_kingdom[i][j]][0] += mapdata[i][j]
            union_info[open_kingdom[i][j]][1] += 1
    union_last = [0] * union_number

    for i in range(len(union_info)):
        if union_info[i][0] != 0 and union_info[i][1] != 0:
            union_last[i] = (union_info[i][0] // union_info[i][1])

    for j in range(N):
        for k in range(N):
            mapdata[j][k] = union_last[open_kingdom[j][k]]

    count += 1
print(count)