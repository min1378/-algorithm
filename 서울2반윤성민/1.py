import sys
sys.stdin = open('1.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            stack.append([i, j])
    min_value = 99999999999
    min_height = 999999999999
    while stack != []:
        W, H = stack.pop()
        W_sum = 0
        H_sum = 0
        temp = [0] * 6
        for i in range(N):
            W_sum += data[W][i]
            temp[data[W][i]] +=1
            H_sum += data[i][H]
            temp[data[i][H]] += 1
        max_count = temp[0]
        for i in range(1, len(temp)):
            if max_count < temp[i]:
                max_count = temp[i]
                height = i
        #height = (W_sum + H_sum) // (2 * N)

        W_value = 0
        H_value = 0
        for i in range(N):
            W_value += abs(data[W][i] - height)
            H_value += abs(data[i][H] - height)
        value = W_value + H_value - abs(data[W][H] - height)

        if min_value > value:

            min_value = value
            min_height = height
        if min_value == value:
            if min_height > height:
                min_height = height

    print("#{} {} {}".format(test_case, min_value, min_height))

