import sys
sys.stdin = open('17837.txt', 'r')
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def solve():

    while count < 1000:
    for mal in mal_list:
        x, y, mode = mal[0], mal[1], mal[2]

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int, input().split())
    data =[list(map(int, input().split())) for _ in range(N)]
    mal_list = [list(map(int, input().split())) for _ in range(K)]
