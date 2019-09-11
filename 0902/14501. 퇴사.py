import sys
sys.stdin = open('14501.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = []
    for i in range(N):
        temp = list(map(int, input().split()))
        data.append(temp)


    stack = []
    for i in range(len(data)):
        if data[i][0] + i <= N:
            stack.append([i+1, data[i], 0])

    print(stack)
    max = 0
    while True:
        print(stack)
        if stack == []:
            break
        day, info, value = stack.pop()



        if day + info[0] - 1 > N :
            if value > max:
                max = value

            continue

        else:
            check = False
            day += info[0]
            value += info[1]



            for i in range(day, N + 1):
                stack.append([i, data[i-1], value])
                check = True
            if check == False:
                if day + info[0] - 1 > N:
                    if value > max:
                        max = value

                    continue

    print("#{} {}".format(test_case, max))



