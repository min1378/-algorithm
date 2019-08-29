import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint
TC =int(input())

for test_case in range(1, TC+1):
    N, M, K = map(int, input().split())
    info = []
    data = [[0]*M for i in range(N)]
    #
    max_count = 0
    for _ in range(K):
        row = list(map(int, input().split()))
        info.append(row)
    # 데이터 입력

    # info에서 하나씩 리스트를 꺼내서 색칠
    for i in info :
        flag = True
        start_col = i[0]
        start_row = i[1]
        end_col = i[2]
        end_row = i[3]
        power = i[4]
        # 색칠할 부분을 검색하여 칠할 색보다 기존 색이 더 크다면 flag = False로 만들고 넘어감
        for j in range(start_col, end_col+1):
            if flag == False:
                break
            for k in range(start_row, end_row+1):
                if data[j][k] > power :
                    flag = False
                    break
        # 기존 색이 크지 않아 flag == True 라면 색칠 시작.
        if flag == True :
            for j in range(start_col, end_col+1):
                for k in range(start_row, end_row+1):
                    data[j][k] = power
    # 음영 11단계를 전부 검색해 count 한다.
    for i in range(11):
        temp = 0
        for j in range(N):
            for k in range(M):
                if data[j][k] == i:
                    temp += 1

        if max_count < temp :
            max_count = temp
    print("#{} {}".format(test_case, max_count))



