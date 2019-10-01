import sys
sys.stdin = open('1486.txt', 'r')

def backtracking(temp, row):
    global min_result
    if min_result <= temp:
        return
    if temp >= B:
        min_result = temp
        return
    if row == N - 1:
        return
    backtracking(temp + height_list[row+1], row + 1)
    backtracking(temp, row + 1)

TC = int(input())
for test_case in range(1, TC+1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))
    min_result = 99999999999

    temp = height_list[0]
    backtracking(temp, 0)
    backtracking(0, 0)
    print("#{} {}".format(test_case, min_result-B))