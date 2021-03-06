import sys
sys.stdin = open('i14500.txt', 'r')
from copy import deepcopy
direction = [(-1, 0), (0, 1), (1, 0)]
direction2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def DFS(x, y, result, list):
    global max_result
    if visited[x][y]:
        return
    if max_result - result >= 1000 * ( 4-len(list) ):
        return
    if len(list) == 4:
        print(list)
        max_result = max(max_result, result)
        return
    visited[x][y] = 1
    if len(list) == 3:
        x, y = list[1]
        for a, b in direction2:
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def connect_check(check):
    visited = [0] * len(check)
    check2 = [check[0]]
    while check2:
        x, y = check2.pop()
        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
                continue
            DFS(xx, yy, result + data[xx][yy], list + [(xx, yy)])

    for a, b in direction:
        xx = x + a
        yy = y + b
        if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
            continue

        DFS(xx, yy, result + data[xx][yy], list + [(xx, yy)])
    visited[x][y] = 0

    
    
    

TC = 22
            if (xx, yy) not in check:
                continue
            index = check.index((xx, yy))
            if visited[index]:
                continue
            visited[index] = 1
            check2.append((xx, yy))
    if sum(visited) == 4:
        return True
    else:
        return False
def distance(check):
    stan = check[0]
    stan2 = check[1]
    for i in check:
        dist = abs(stan[0] - i[0]) + abs(stan[1] - i[1])
        dist2 = abs(stan2[0] - i[0]) + abs(stan2[1] - i[1])
        if dist > 3 or dist2 > 3:
            return False
    return True
def comb(index, temp):
    global max_result
    if len(temp) > 1:
        check = []
        for el in temp:
            check.append((el//M, el % M))
        if distance(check) == False:
            return
    if len(temp) == 4:
        check = []
        for el in temp:
            check.append((el//M, el % M))
        if connect_check(check) :
            result = 0
            for el in check:
                result += data[el[0]][el[1]]
            max_result = max(max_result, result)
        return
    
    for i in range(index, N * M):
        if visited[i]:
            continue
        visited[i] = 1
        comb(i + 1, temp + [i])
        visited[i] = 0

#TC = 19
#for test_case in range(1, TC+1):
max_result = 0
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        for line in visited:
            print(line)
        DFS(i, j, data[i][j], [(i, j)])
print(max_result)
