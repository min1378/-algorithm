import sys
sys.stdin = open('17472.txt', 'r')
import itertools

#TC = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1 :
        return True
    return False

def DFS1(x, y):
    global union_number
    data[x][y] = union_number
    visited[x][y] = 1
    s = [(x, y)]
    while s:
        x, y = s.pop()
        data[x][y] = union_number
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy):
                continue
            if visited[xx][yy] == False and data[xx][yy] == 1:
                s.append((xx, yy))
                visited[xx][yy] = True
    return

def four_check(x, y):
    count = 0
    for mode in range(4):
        xx = x + dx[mode]
        yy = y + dy[mode]
        if isWall(xx, yy) == False:
            if data[xx][yy] :
                count += 1
        else:
            count += 1

    if count == 4:
        return True
    else:
        return False


def cal_count(i, j):
    visited[i][j] = 1
    check = my_land = data[i][j]
    for mode in range(4):
        count = 0
        x = i
        y = j
        while True:
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy) :
                count = -1
                break

            if data[xx][yy]:
                check = data[xx][yy]
                break

            else:
                count += 1
                x = xx
                y = yy

        if count < 2 or check == my_land:
            continue

        else:
            #print([i, j],[xx, yy], my_land,"번 지역에서", check,"번 " , count)
            if min_list[my_land][check] == 0:
                min_list[my_land][check] = count
            else:
                min_list[my_land][check] = min(count, min_list[my_land][check])





#for test_case in range(1, TC+1):
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited =[[0] * M for _ in range(N)]
union_number = 1

for i in range(N):
    for j in range(M):
        if data[i][j] == 1 and visited[i][j] == False:
            DFS1(i, j)
            union_number += 1

visited =[[0] * M for _ in range(N)]
min_list = [[0]*union_number for _ in range(union_number)]
min_dist = 10000000
for i in range(N):
    for j in range(M):
        if data[i][j]:
            if four_check(i, j) == False and visited[i][j] == 0:
                cal_count(i, j)

last = []
for i in range(union_number):
    for j in range(union_number):
        if min_list[i][j] :
            last.append([i, j, min_list[i][j]])
print(last)
for comb in itertools.combinations(last, union_number - 2):
    check = []
    temp = 0
    union = [i for i in range(union_number)]
    flag = True
    for i in range(union_number - 2):
        start, end, count = comb[i]
        for j in range(len(union)):
            if union[j] == union[start]:
                union[j] = union[end]
        temp += count
    union.pop(0)
    for i in union:
        if i != union[-1]:
            flag = False

    if flag :
        min_dist = min(min_dist, temp)
if min_dist == 10000000:
    min_dist = -1
print(min_dist)
