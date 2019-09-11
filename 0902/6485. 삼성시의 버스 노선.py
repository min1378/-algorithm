import sys
sys.stdin = open('6485.txt', 'r')
TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    datas = []
    for i in range(N):
        temp = list(map(int, input().split()))
        datas.append(temp)

    P = int(input())
    C = []
    for i in range(P):
        C.append(int(input()))


    result = ''
    for _ in range(P):
        count = 0
        temp = C.pop(0)
        for data in datas:
            start = data[0]
            end = data[1]
            if start <= temp and end >= temp:
                count +=1
        result += str(count) + ' '

    print("#{} {}".format(test_case, result))
