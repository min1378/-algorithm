import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint 


def SearchEdge(data):
    temp = []
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j] == 1 and temp == []:
                    temp.append([i,j])
                    rcount = 0
                if j < lend(data)-1 and data[i][j]==1 and data[i][j+1] == 0 :
                    dcount += 1
                elif j < lend(data)-1 and data[i][j]==1 and data[i][j+1] == 0 and data[]:








T = 1

for test_case in range(1, T + 1):
    #입력 받기
    W = int(input())
    insert = list(map(int, input().split()))

    u = insert[0]
    v = insert[1]
    w = insert[2]
    x = insert[3]
    y = insert[4]
    data = []
    # W X W  data 행렬 만들기
    for i in range(W):
        temp = list(map(int, input().split()))
        data.append(temp)
    clone_data = data
    #print('#{} {}'.format(test_case, result))