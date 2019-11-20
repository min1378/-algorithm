import sys
sys.stdin = open('5120.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int, input().split())
    datas = list(map(int, input().split()))
    start = 0
    start_number = datas[0]
    for _ in range(K):
        start += M
        if start > len(datas) :
            start -= len(datas)

        if start == len(datas):
            datas.append(datas[-1]+start_number)
        else:
            datas.insert(start, datas[start] + datas[start-1])

    result_list = list(reversed(datas))
    result_list2 = result_list[0:10]
    result = ''
    for i in range(len(result_list2)):
        result += str(result_list2[i]) + ' '

    print("#{} {}".format(test_case, result.strip() ))