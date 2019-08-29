import sys
from pprint import pprint
sys.stdin = open('2.txt', 'r')

TC = int(input())

def iswall(x, y):
    if x < - 1000 or x > 1000 :
        return True
    if y < - 1000 or y > 1000 :
        return True
    return False



for test_case in range(1, TC+1):
    N = int(input())
    info = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        info.append(temp)
    count = 0

    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]
    used = [False] * N

    temp = [i for i in range(N)]
    round = 0

    while True:

        if len(info) < 2 :
            break

        temp3 = []

        for i in range(len(info)):
            x = info[i][0]
            y = info[i][1]
            mode = info[i][2]
            x = x + dx[mode]
            y = y + dy[mode]
            info[i][0] = x
            info[i][1] = y
            if iswall(info[i][0], info[i][1]) == True:
                continue
            else:
                temp3.append([info[i][0], info[i][1], info[i][2], info[i][3]])
        info = []
            #print("round{} {} x={} y={}".format(round, i, x, y))
        # temp2 = []

        # dic = {}
        # for x, y, direc, k in info:
        #     if dic.get((x, y)):
        #         dic[(x, y)].append((direc, k))
        #     else:
        #         dic[(x, y)] = [(direc, k)]
        #
        # info = []
        # for key, value in dic.items():
        #     if len(dic[key]) > 1:
        #         for direc, k in dic[key]:
        #             count += k
        #     else:
        #         info.append([key[0], key[1], value[0][0], value[0][1]])

        temp4 = {}

        for x, y, mode, energy in temp3:
            if temp4.get((x, y)):
                temp4[(x, y)].append((mode, energy))
            else:
                temp4[(x, y)] = [(mode, energy)]


        for key, value in temp4.items():
            if len(temp4[key]) > 1:
                for mode, energy in temp4[key]:
                    count += energy
            else:
                info.append([key[0], key[1], value[0][0], value[0][1]])

        # for i in range(len(temp)-1) :
        #     for j in range(i, len(temp)) :
        #         if i == j :
        #             continue
        #         if info[temp[i]][0]==info[temp[j]][0] and info[temp[i]][1]==info[temp[j]][1]:
        #             if temp[i] not in temp2 :
        #                 temp2.append(temp[i])
        #             if temp[j] not in temp2 :
        #                 temp2.append(temp[j])

        if round == 4000:
            break


    print("#{} {} {}회".format(test_case, count, round))

