import sys
sys.stdin = open('1242.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    for i in range(N):
        temp = str(input())
        for j in range(len(temp)):
            if temp[j] != '0':
                break
        check = temp
