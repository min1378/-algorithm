# import sys
# sys.stdin = open('1941.txt', 'r')
import sys
sys.stdin = open('1941.txt', 'r')
# def isWall(x, y):
#     if x < 0 or x > 4 or y < 0 or y > 4 :
#         return True
#     return False
# def move(x, y, members):
#     global count
#     if members.count('Y') > 3:
#         return
#     if len(members) == 7:
#         if members.count('S') > 3 :
#             print(members)
#             count += 1
#         return
#     for mode in range(4):
#         xx = x + dx[mode]
#         yy = y + dy[mode]
#         if isWall(xx, yy):
#             continue
#         if visited[xx][yy]:
#             continue
#         visited[xx][yy] = 1
#         move(xx, yy, members + [data[xx][yy]])
#         visited[xx][yy] = 0
#
# data = [list(input()) for _ in range(5)]
# dasom = []
# count = 0
# for i in range(5):
#     for j in range(5):
#         if data[i][j] == 'S':
#             dasom.append([i, j])
# check = []
# visited = [[0] * 5 for _ in range(5)]
# for da in dasom:
#     x = da[0]
#     y = da[1]
#     move(x, y, [data[x][y]])
# print(count)
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def isWall(x, y):
    if x < 0 or x > 4 or y < 0 or y > 4 :
        return True
    return False

def DFS():
    visit = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                count = 0
                stack = [[i, j]]
                visit[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    count += 1
                    if count == 7:
                        return True
                    for mode in range(4):
                        xx = x + dx[mode]
                        yy = y + dy[mode]
                        if isWall(xx, yy):
                            continue
                        if visit[xx][yy]:
                            continue
                        if visited[xx][yy]:
                            stack.append([xx, yy])
                            visit[xx][yy] = 1

                return False
def comb(index, members_coordi, members):
    global count
    if members.count('Y') > 3:
        return
    if len(members) == 7:
        result = DFS()
        if result:
            count += 1
        return
    for i in range(index, len(check)):
        if visited[i // 5][i % 5]:
            continue
        visited[i // 5][i % 5] = 1
        comb(i + 1, members_coordi + [check[i]], members + [data[check[i][0]][check[i][1]]])
        visited[i // 5][i % 5] = 0

data = [list(input()) for _ in range(5)]
check = []
count = 0
for i in range(5):
    for j in range(5):
        check.append([i, j])
visited = [[0] * 5 for _ in range(5)]
comb(0, [], [])
print(count)