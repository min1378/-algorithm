TC = int(input())

def iswall(x, y):
    if x < - 1000 or x > 1000 :
        return True
    if y < - 1000 or y > 1000 :
        return True
    return False

def simul(info, temp):
    global count_a
    global count
    global used
    global dx
    global dy
    if len(temp) < 2:
        return
    temp3 = []

    for i in temp:
        if iswall(info[i][0], info[i][1]) == True or used[i] == True:
            temp3.append(i)

    if temp3 != []:
        for i in temp3:
            temp.remove(i)

    for i in temp:
        x = info[i][0]
        y = info[i][1]
        mode = info[i][2]
        x = x + dx[mode]
        y = y + dy[mode]
        info[i][0] = x
        info[i][1] = y
        # print("round{} {} x={} y={}".format(round, i, x, y))
    temp2 = []
    for i in range(len(temp)):
        for j in range(i, len(temp)):
            if i == j:
                continue

            result = abs(info[temp[i]][0] - info[temp[j]][0]) + abs(info[temp[i]][1] - info[temp[j]][1])
            if result == 0:
                if temp[i] not in temp2:
                    temp2.append(temp[i])
                if temp[j] not in temp2:
                    temp2.append(temp[j])
    if temp2 != []:

        for i in temp2:
            count += info[i][3]
            used[i] = True
    count_a += 1
    print(count_a)
    return simul(info, temp)

for test_case in range(1, TC+1):
    N = int(input())
    info = []
    count_a = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        info.append(temp)
    count = 0
    round = 0
    dx = [0, 0, -0.5, 0.5]
    dy = [0.5, -0.5, 0, 0]
    used = [False] * N

    temp = [i for i in range(N)]

    simul(info, temp)
    print(count)