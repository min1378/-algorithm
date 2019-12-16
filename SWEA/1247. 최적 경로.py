import sys
sys.stdin = open('1247.txt')
import itertools
TC = int(input())
def cal_distance(list1, list2):
   return (abs(list1[0] - list2[0]) + abs(list1[1] - list2[1]))

def min_distance(list, distance):
    global min_dist
    if distance > min_dist:
        return
    if len(list) == N:
        distance += cal_distance(my, custom[list[-1]])

        if distance < min_dist:
            min_dist = distance

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        min_distance(list + [i], distance + cal_distance(custom[i], custom[list[-1]]))
        visited[i] = False

for test_case in range(1, TC+1):
    N = int(input())
    temp = list(map(int, input().split()))
    company = [temp[0], temp[1]]
    my = [temp[2], temp[3]]
    custom = []
    for i in range(4, N*2+4):
        if i % 2 == 0:
            custom.append([temp[i], temp[i+1]])
    min_dist = 999999999

    visited = [False] * N

    for i in range(N):
        visited[i] = True
        min_distance([i], cal_distance(company, custom[i]))
        visited[i] = False

    print("#{} {}".format(test_case, min_dist))