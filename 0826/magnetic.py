import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

TC = 10
for tc in range(1, TC+1):
    width = int(input())
    mymap = [[0] * (width) for _i in range(width)]
    count = 0
    for i in range(width):
        data = list(map(int, input().split()))
        mymap[i] = data

    # for i in range(len(data)):
    #     mymap[i//width][i % width] = data[i]
    for i in range(len(mymap)):
        temp = []
        for j in range(100):
            if mymap[j][i] != 0 :
                temp.append(mymap[j][i])
        #print(temp)

        for j in range(len(temp)-1):
            if temp[j] == 1 and temp[j+1] == 2 :
                count += 1

    print('#{} {}'.format(TC, count))