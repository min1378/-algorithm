# import sys
# sys.stdin = open("max_input.txt", "r")

def n_sum(M, a) :
    result_1 = 0
    for i in range(M) :
        result_1 += numbers[a+i]
    return result_1
T = int(input())
for test_case in range(1, T + 1):
    info = list(map(int, input().split()))
    numbers = list(map(int, input().split()))   
    N = info[0]
    M = info[1]
    n_max = n_sum(M, 1)   
    n_min = n_sum(M, 1)
    for i in range(0, N-M+1) :
        if n_max < n_sum(M, i):            
            n_max = n_sum(M, i)
        if n_min > n_sum(M, i):
            n_min = n_sum(M, i)
    result = n_max - n_min
    print('#{} {}'.format(test_case, result))