#import sys
import itertools
import copy
#from pprint import pprint
def move():
    for i in range(N-1, -1, -1):
        if i == N-1:
            continue
        else:
            clone_data[i+1] = copy.deepcopy(clone_data[i])
    clone_data[0] = [0] * M

def cal(archer, enermy):
    distance = abs(archer[0] - enermy[0]) + abs(archer[1] - enermy[1])
    return distance
def attack():
    death = []

    for k in range(3):
        max_distance = D
        death_enermy = 0
        for i in range(N - 1, -1, -1):
            if 1 in clone_data[i]:
                for j in range(M-1, -1, -1):
                    if clone_data[i][j] == 1:
                        distance = cal(archer[k],[i, j])
                        if distance <= max_distance:
                            if distance == max_distance:
                                if death_enermy != 0:
                                    if death_enermy[1] > j:
                                        death_enermy = [i, j]
                                else:
                                    death_enermy = [i, j]
                            else:
                                max_distance = distance
                                death_enermy = [i, j]
        if death_enermy != 0:
            death.append(death_enermy)
    temp2 = []
    for de in death:
        if de not in temp2:
            temp2.append(de)

    return temp2

#sys.stdin = open('17135.txt', 'r')
#TC = int(input())
#for test_case in range(1, TC+1):
N, M, D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
archer_location = [i for i in range(M)]
stack = list(itertools.combinations(archer_location, 3))
#print(stack)
max_count = 0
while stack != []:
    count = 0
    clone_data = copy.deepcopy(data)
    first, second, third = stack.pop()
    #print(first, second, third)
    #print(D)
    archer = []
    first = [N,first]
    second = [N, second]
    third = [N, third]
    archer.append(first)
    archer.append(second)
    archer.append(third)
    #print("공격전")
    #pprint(clone_data)

    for round in range(N):

        death = attack()
        #print("사망자명단")
        #print(death)
        count += len(death)
        for _ in range(len(death)):
            temp = death.pop()

            i = temp[0]
            j = temp[1]
            clone_data[i][j] = 0
        #print("공격후")
        #pprint(clone_data)

        move()
        #print("이동후")
        #pprint(clone_data)
        check = 0
        for line in clone_data:
            if 1 not in line:
                check += 1

        if check == N:
            break
    #print("총 죽인 횟수")
    #print(count)
    if max_count < count:
        max_count = count


print(max_count)