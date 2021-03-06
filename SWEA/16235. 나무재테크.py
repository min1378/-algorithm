import sys
import itertools

sys.stdin = open('16235.txt', 'r')
def isWall(x, y):
    if x > N-1 or x < 0:
        return True
    if y > N-1 or y < 0:
        return True
    return False

def spring():
    dead_tree = []
    a = len(tree_info)
    for _ in range(a):
        x, y, age = tree_info.pop(0)
        if mapdata[x][y] >= age:
            mapdata[x][y] -= age
            age +=1
            tree_info.append([x, y, age])
        else :
           dead_tree.append([x, y, age])

    return dead_tree

def summer(dead_tree):
    for _ in range(len(dead_tree)):
        x, y, age = dead_tree.pop()
        mapdata[x][y] += age // 2

def fall():
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(len(tree_info)):
        if tree_info[i][2] % 5 == 0:
            x = tree_info[i][0]
            y = tree_info[i][1]
            for mode in range(8):
                test_x = x + dx[mode]
                test_y = y + dy[mode]
                if isWall(test_x, test_y) == False:
                    tree_info.append([test_x, test_y, 1])



def winter():
    for i in range(N):
        for j in range(N):
            mapdata[i][j] += food[i][j]

TC=int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int, input().strip().split())
    food = [list(map(int , input().strip().split())) for _ in range(N)]
    mapdata = [[5] * N for _ in range(N)]



    tree_info = [list(map(int, input().strip().split())) for _ in range(M)]






    for i in tree_info:
        i[0] -= 1
        i[1] -= 1

    for _ in range(K):
         sorted(tree_info, key=lambda tree_age: tree_age[2])
         dead_tree = spring()
         summer(dead_tree)
         fall()
         winter()

    print(len(tree_info))

