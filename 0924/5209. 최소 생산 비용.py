import sys
sys.stdin = open('5209.txt', 'r')

def find_min_sum(y, min_sum):
    global result_min
    for i in range(N):
        if not select_limit[i]:
            if y < N - 1 and result_min > data[y][i] + min_sum:
                select_limit[i] = True
                result_min = min(result_min, find_min_sum(y + 1, data[y][i] + min_sum))
                select_limit[i] = False
            else:
                result_min = min(result_min, min_sum + data[y][i])
    return result_min

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    select_limit = [False] * N
    result_min = 999999999999
    result_min = find_min_sum(0,0)
    print("#{} {}".format(test_case, result_min))
