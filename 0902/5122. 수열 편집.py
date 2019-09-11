import sys
sys.stdin = open('5122.txt', 'r')
TC = int(input())
for test_case in range(1, TC + 1):
    N, M, L = map(int, input().split())

    datas = list(map(int, input().split()))
    check = []
    for _ in range(M):
        temp = list(map(str, input().split()))
        check.append(temp)

    for checked in check:
        for i in range(len(checked)):
            if checked[i].isdigit():
                checked[i] = int(checked[i])

    for checked in check:
        if checked[0] == 'I':
            datas.insert(checked[1], checked[2])
        elif checked[0] == 'D':
            datas.pop(checked[1])
        elif checked[0] == 'C':
            datas[checked[1]] = checked[2]


    if L > len(datas) - 1:
        result = -1
    else:
        result = datas[L]

    print("#{} {}".format(test_case, result))

