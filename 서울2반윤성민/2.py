import sys
import itertools
import copy
sys.stdin = open('2.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(10)]
    robot_location = []
    fruits_location = []
    for i in range(10):
        for j in range(10):
            if 0 < data[i][j] < 7:
                fruits_location.append([j, i])
            elif data[i][j] == 9:
                robot_location.append([j, i])

    #print(robot_location)
    #print(fruits_location)
    fruits_index = [0, 1, 2, 3, 4, 5]
    stack = list(itertools.permutations(fruits_index, 6))
    #print(stack)
    min_count = 9999999999
    while stack != []:
        temp = stack.pop()
        count = 0
        for i in range(len(temp)):
           robot_x = robot_location[i][0]
           robot_y = robot_location[i][1]
           fruit_x = fruits_location[temp[i]][0]
           fruit_y = fruits_location[temp[i]][1]
           distance = abs(robot_x - fruit_x) + abs(robot_y - fruit_y)
           count += distance

        if min_count > count:
            min_count = count

    print("#{} {}".format(test_case,min_count))