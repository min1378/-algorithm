import sys
from pprint import pprint
sys.stdin = open('6109.txt', 'r')
TC = int(input())
def binary_check(number):
    check = bin(number)
    if 1 == check.count('1'):
        return True

    return False
def rotate(m, d):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-r][N-1-c] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret

def push(clone_mapdata):
    result = []
    for y in range(N):
        sero = []

        for x in range(N):
            if clone_mapdata[x][y] != 0:
                sero.append(clone_mapdata[x][y])
        # print(sero)
        count = 0
        ans = []
        while count < len(sero):

            if count == len(sero) - 1:
                ans.append(sero[count])
                count += 1

            elif sero[count] == sero[count + 1] and count < len(sero) - 1:
                ans.append(sero[count] * 2)
                count += 2

            else:
                ans.append(sero[count])
                count += 1
        # print(ans)
        while len(ans) != N:
            ans.append(0)
        result.append(ans)
        # print(answer)
        continue
    return result
def change(mapdata, mode):

    if mode == "up":

        clone_mapdata = push(mapdata)
        temp = push(clone_mapdata)
        result = temp
    elif mode == "right":

        clone_mapdata = rotate(mapdata, 3)
        temp = push(clone_mapdata)
        result = rotate(temp, 2)
    elif mode == "down":

        clone_mapdata = mapdata
        temp = push(clone_mapdata)

        result = rotate(temp, 3)
    elif mode == "left":

        clone_mapdata = rotate(mapdata, 3)
        temp = push(clone_mapdata)

        result = rotate(temp, 4)

    return result



for test_case in range(1, TC+1):
    N, mode = map(str, input().split())
    N = int(N)
    mapdata = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    pprint(mapdata)



    final = change(mapdata, mode)

    pprint(final)


    print("#{}".format(test_case))
    for line in final:
        ans = ''
        for i in line:
            ans += str(i) + ' '

        print(ans)

