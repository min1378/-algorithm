import sys
sys.stdin = open('5110.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    first_data = list(map(int, input().split()))
    for _ in range(M-1):
        first_len = len(first_data)
        data = list(map(int, input().split()))
        for i in range(len(first_data)):
            if first_data[i] > data[0]:
                first_data[i:0] = data
                break
        if  first_len == len(first_data):
            first_data.extend(data)



    temp = list(reversed(first_data))
    temp2 = temp[0:10]

    result = ''
    for i in range(len(temp2)):
        result += str(temp2[i]) +" "

    print("#{} {}".format(test_case, result.strip()))



