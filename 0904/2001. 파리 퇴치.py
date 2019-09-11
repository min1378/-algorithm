import sys
from pprint import pprint
sys.stdin = open('2001.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    temp +=data[k][l]

            if temp > result:


                result = temp

    print("#{} {}".format(test_case, result))