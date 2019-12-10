import sys

sys.stdin = open('17822.txt', 'r')
TC = int(input())
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(check_list):
    global N, M, T
    global result
    for q in range(T):

        x = check_list[q][0]
        d = check_list[q][1]
        k = check_list[q][2]
        for qq in range(N):
            if (qq+1) % x :
                continue

            if d == 0:
                    data[qq].rotate(k)

            elif d == 1:
                    data[qq].rotate(-k)

        check = False
        del_list = []
        for x in range(N):
            for y in range(M):
                if data[x][y] == 0:
                    continue
                for mode in range(4):
                    xx = x + dx[mode]
                    yy = y + dy[mode]
                    if yy == -1:
                        yy = M-1
                    if yy == M:
                        yy = 0
                    if xx < 0 or xx > N - 1 :
                        continue
                    if data[x][y] == data[xx][yy]:
                        del_list.append([xx, yy])
                        check = True
        for i in range(len(del_list)):
            xx, yy = del_list[i]
            data[xx][yy] = 0

        if check == False:
            temp = 0
            zero = 0
            for i in range(len(data)):
                temp += sum(data[i])
                zero += data[i].count(0)
            if (N * M - zero) == 0:
                temp = 0
            else:
                temp /= (N * M - zero)

            for i in range(N):
                for j in range(M):
                    if data[i][j] == 0:
                        continue
                    if data[i][j] > temp:
                        data[i][j] -= 1
                    elif data[i][j] < temp:
                        data[i][j] += 1


        if q == T-1:
            temp = 0
            for i in range(len(data)):
                temp += sum(data[i])
            result = temp

#for test_case in range(1, TC+1):
result = 0
N, M, T = map(int,input().split())
data = [deque(map(int, input().split())) for _ in range(N)]
check_list = [list(map(int, input().split())) for _ in range(T)]
solve(check_list)
print(result)

