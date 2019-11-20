import sys
sys.stdin = open('5208.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    info = list(map(int, input().split()))
    N = info.pop(0)

    data = []
    for i in range(N-1):
        data.append([i+1, info[i]])

    start = data[0][0]
    tank = data[0][1]
    count = 0
    end = N
    stack = []
    min_result = N+1
    for i in range(start + 1, start + tank + 1):
        stack.append([data[i-1][0], data[i-1][1], count])

    while True:

        if stack == []:
            break
        start, oil, count  = stack.pop()
        if count >= min_result :
            continue
        if start >= N or start + oil >= N :
            if count < min_result :
                min_result = count + 1
                continue

        else:
            tank = oil
            count += 1

            maximum = start + tank + 1
            if maximum > end:
                maximum = end
            for i in range(start + 1, maximum):
                stack.append([data[i - 1][0], data[i - 1][1], count])


    print("#{} {}".format(test_case, min_result))

