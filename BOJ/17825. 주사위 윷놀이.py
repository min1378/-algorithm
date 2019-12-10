import sys
sys.stdin = open('17825.txt', 'r')

TC = int(input())

def solve(index):

    for i in range(len(mal)):

        solve(i+)
        


for test_case in range(1, TC+1):
    dice_list = list(map(int, input().split()))
    score = [0, 2, 4, 6, 8,
             10, 12, 14, 16, 18,
             20, 22, 24, 26, 28,
             30, 32, 34, 36, 38,
             40, 0, 13, 16, 19,
             25, 26, 27, 28, 30,
             35]
    mal = [1, 1, 1, 1]
    # solve(0)