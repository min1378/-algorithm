#import sys
from pprint import pprint
import itertools
import copy
#sys.stdin = open('15686.txt', 'r')

def min_distance():
    seller = []
    result = []
    for i in range(N):
        for j in range(N):
            if clone_mapdata[i][j] == 2:
                seller.append([i, j])
    #print(seller)
    for j in range(len(home)):
        temp = []
        for i in range(len(seller)):
            temp.append(abs((seller[i][0] + 1) - (home[j][0] + 1)) + abs((seller[i][1] + 1) - (home[j][1] + 1)))
        result.append(min(temp))
    return result




# TC = int(input())
# for test_case in range(1, TC+1):
N, M = map(int, input().split())
mapdata = [list(map(int, input().split())) for _ in range(N)]
#print(N, M)
#pprint(mapdata)

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if mapdata[i][j] == 2:
            chicken.append([i, j])
        elif mapdata[i][j] == 1:
            home.append([i, j])


#print(M)
#print(chicken)

min_chicken_distance = 10000000
for i in range(len(chicken)-M, len(chicken)):
    c = list(itertools.combinations(chicken, i))
    #print("C")
    #print(c)
    while True:

        if c == []:
            break

        clone_mapdata = copy.deepcopy(mapdata)

        info = c.pop(0)
        #print(info)
        for i in range(len(info)):
            clone_mapdata[info[i][0]][info[i][1]] = 0

        #print("폐업후")
        #pprint(clone_mapdata)
        result = min_distance()
        #print(result)
        temp2 = sum(result)
        #print("결과값")
        #print(temp2)
        if min_chicken_distance > temp2:
            min_chicken_distance = temp2


print(min_chicken_distance)