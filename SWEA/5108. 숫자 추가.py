import sys
sys.stdin = open('5108.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M, L = map(int, input().split())
    first_data = list(map(int, input().split()))
    datas = [list(map(int, input().split())) for i in range(M)]
    for data in datas:
        first_data.insert(data[0], data[1])

    print("#{} {}".format(test_case, first_data[L]))