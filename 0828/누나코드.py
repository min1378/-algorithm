import sys
sys.stdin = open('2.txt', 'r')
from pprint import pprint
T = 1
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    board = [[0 for j in range(M)] for i in range(N)]

    for k in range(K):
        start_x, start_y, end_x, end_y, m = map(int, input().split())
        check = 0
        if check == 1:
            break
        for a in range(start_x, end_x+1):
            if check == 1:
                break
            for b in range(start_y, end_y+1):
                if board[a][b] > m:
                    check = 1
                    break
        else:
            check2 = 0
            if start_x == end_x:
                if start_y == end_y:
                    if m >= board[start_x][start_y]:
                        board[start_x][start_y] = m
                else:
                    if check2 == 1:
                        break
                    for e in range(start_y, end_y+1):
                        if board[start_x][e] > m:
                            check2 = 1
                            break
                    else:
                        for z in range(start_y, end_y + 1):
                            board[start_x][z] = m
            elif start_y == end_y:
                if check2 == 1:
                    break
                for f in range(start_x, end_x+1):
                    if board[f][start_y] > m:
                        check2 = 1
                        break
                else:
                    for o in range(start_x, end_x+1):
                        board[o][start_y] = m
            else:
                for c in range(start_x, end_x + 1):
                    for d in range(start_y, end_y + 1):
                        board[c][d] = m
        print("{}번째".format(k))
        pprint(board)
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0
    cnt_5 = 0
    cnt_6 = 0
    cnt_7 = 0
    cnt_8 = 0
    cnt_9 = 0
    cnt_10 = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt_0 += 1
            elif board[i][j] == 1:
                cnt_1 += 1
            elif board[i][j] == 2:
                cnt_2 += 1
            elif board[i][j] == 3:
                cnt_3 += 1
            elif board[i][j] == 4:
                cnt_4 += 1
            elif board[i][j] == 5:
                cnt_5 += 1
            elif board[i][j] == 6:
                cnt_6 += 1
            elif board[i][j] == 7:
                cnt_7 += 1
            elif board[i][j] == 8:
                cnt_8 += 1
            elif board[i][j] == 9:
                cnt_9 += 1
            elif board[i][j] == 10:
                cnt_10 += 1
    cnt_best = max(cnt_0,cnt_1,cnt_2,cnt_3,cnt_4,cnt_5,cnt_6,cnt_7,cnt_8,cnt_9,cnt_10)
    # print(cnt_0,cnt_1,cnt_2,cnt_3,cnt_4,cnt_5,cnt_6,cnt_7,cnt_8,cnt_9,cnt_10)
    # print(board)
    print('#{} {}'.format(tc, cnt_best))