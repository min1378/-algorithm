import sys
sys.stdin = open('2805.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = [str(input()) for _ in range(N)]

    print(N)
    mid = N//2

    value = 0
    # if N == 1:
    #     value = int(data[0][0])
    # elif N == 3:
    #     value += int(data[0][1]) + int(data[1][0]) + int(data[1][1]) + int(data[1][2]) + int(data[2][1])
    # else:
    for i in range(mid):
        for j in range(mid-i, N-mid+i):
            value +=int(data[i][j])


    for i in range(mid, N):
        for j in range(0+i-mid, N-i+mid):
            value +=int(data[i][j])


    print("#{} {}".format(test_case, value))
