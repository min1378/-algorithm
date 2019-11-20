import sys
sys.stdin = open('1979.txt', 'r')
def check(mode):
    #가로
    check = []
    if mode == 1:
        line_number = 0
        for line in mapdata:
            i = 0

            while i <= N - 1:
                if line[i] == 1:

                    count = 1
                    if i == N-1:
                        check.append([line_number, count])
                        break
                    for j in range(i+1, N):
                        if line[j] != 1 :
                            check.append([line_number, count])
                            i = j
                            break
                        elif j == N-1:
                            count += 1
                            check.append([line_number, count])
                            i = j
                            break
                        else:
                            count += 1
                i += 1
            line_number += 1
    #세로

    elif mode == 2:
        line_number = 0
        for i in range(N):
            j = 0

            while j < N - 1:
                if mapdata[j][i] == 1:
                    count = 1
                    if j == N-1:
                        check.append([line_number, count])
                        break
                    for k in range(j+1, N):
                        if mapdata[k][i] != 1:
                            check.append([line_number, count])
                            j = k
                            break
                        elif k == N-1:
                            count += 1
                            check.append([line_number, count])
                            j = k
                            break
                        else:

                            count += 1
                j += 1
            line_number += 1

    return check
TC = int(input())
for test_case in range(1, TC+1):
    N, L = map(int, (input().split()))

    mapdata = [list(map(int, input().split())) for _ in range(N)]

    width = check(1)
    length = check(2)
    count = 0
    for w in width:
        if w[1] == L :
            count += 1
    for l in length:
        if l[1] == L :
            count += 1




    print("#{} {}".format(test_case, count))