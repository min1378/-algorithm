import sys
import itertools
import copy

from pprint import pprint
sys.stdin = open('3.txt', 'r')
TC = int(input())
def distance(go):
    x = mineral_location[go][0][0]
    y = mineral_location[go][0][1]
    mine = mineral_location[go][1]
    scv_x = scv_info[0]
    scv_y = scv_info[1]
    length = (abs(x - scv_x) + abs(y - scv_y)) * 2
    return mine, length
for test_case in range(1, TC+1):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    mineral_location = []
    for i in range(N):
        for j in range(M):
            if data[i][j] > 1:
                mineral_location.append([[i, j], data[i][j]])
            elif data[i][j] == 1:
                scv_info = [i, j]

    loce = [i for i in range(len(mineral_location))]
    stack = []
    stack.append([C] + [loce] + [0])
    max_mineral = 0
    while stack != []:

        energy, mineral_index, mineral = stack.pop()

        if mineral_index == [] or energy == 0:
            if max_mineral < mineral:
                max_mineral = mineral
            continue
        temp = []
        for i in range(len(mineral_index)):
            go = mineral_index[i]
            mine, length = distance(go)
            #print(energy, length, mineral_index)
            if energy >= length:
                temp.append(i)

        for i in range(len(temp)-1, -1, -1):
            temp2 = copy.deepcopy(temp)
            i_index = temp2.pop(i)
            go = mineral_index[i_index]
            mine, length = distance(go)
            new_energy = energy - length
            new_mine = mineral + mine
            new = [new_energy] + [temp2] + [new_mine]
            stack.append(new)




    print(max_mineral)