import sys
import copy
from pprint import pprint
import itertools
sys.stdin = open('14502.txt', 'r')
def isWall(x, y):
    if x > N-1 or x < 0 :
        return True
    if y > M-1 or y < 0 :
        return True
    return False
def comb(k, now, temp):
   global result
   if k == 3:
       result.append(temp)
   else:
       for i in range(now+1, len(stack)+1):
           comb(k+1, i, temp + [i])
def DFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    #check = []
    stack = [[x, y]]
    while True:
        if stack == []:
            #return check
            return
        x, y = stack.pop()
        for mode in range(4):
            test_x = x + dx[mode]
            test_y = y + dy[mode]
            if isWall(test_x, test_y) == False and clone_map[test_x][test_y] == 0: #and [test_x, test_y] not in check and [test_x, test_y] not in temp:
                stack.append([test_x, test_y])
                #check.append([test_x, test_y])
                clone_map[test_x][test_y] = 2

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    datamap = [list(map(int, input().split())) for _ in range(N)]

    max = 0



    stack = []
    virus = []
    #zero_count = 0
    for i in range(N):
        for j in range(M):
            if datamap[i][j] == 2:
                virus.append([i, j])
            elif datamap[i][j] == 0:
                stack.append([i, j])
                #zero_count +=1

    max = 0
    #print(stack)
    #print(len(stack))
    zz = [i for i in range(len(stack))]
    #print(zz)
    d = list(itertools.combinations(zz, 3))
    print(d)
    #print(len(d))
    while True:
        #count = zero_count
        if d == []:
            break

        clone_map = copy.deepcopy(datamap)
        clone_virus = copy.deepcopy(virus)
        #pprint(clone_map)
        first, second, third = d.pop()
        #print(first, second, third)
        clone_map[stack[first][0]][stack[first][1]] = 1
        clone_map[stack[second][0]][stack[second][1]] = 1
        clone_map[stack[third][0]][stack[third][1]] = 1
        # temp = []
        #pprint(clone_map)
        for _ in range(len(virus)):
            virus_x, virus_y = clone_virus.pop()
            DFS(virus_x, virus_y)
            # virus_count = DFS(virus_x, virus_y)
            # temp += virus_count
            # if len(temp) + 3 == count:
            #     break
            # for x, y in virus_count:
            #     if clone_map[x][y] == 0:
            #         clone_map[x][y] = 2
        #pprint(clone_map)
        # count -= (len(temp) + 3)
        count = 0
        for line in clone_map:
            count +=line.count(0)

        if count > max:
            max = count

    print(max)

