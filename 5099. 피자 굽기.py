import sys
sys.stdin = open('5099.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    Ci = []
    count = 0
    Cs = []
    for i in range(len(temp)):
        Ci.append([temp[i], i+1])

    stack = []
    temp2 = 0

    for i in range(N):
        temp = Ci.pop(0)
        stack.append(temp)

    flag = True
    while flag :

        for i in range(N):

            temp = stack[i]
            if temp[0] != -1:
                temp[0] = temp[0] // 2
                stack[i] = temp

        for i in range(N):
            temp = stack.pop(0)
            if temp[0] == 0 :
                if len(Ci) > 0:
                    temp2 = Ci.pop(0)
                    stack.append(temp2)
                else:
                    stack.append([-1])

                Cs.append(temp)

            else:
                stack.append(temp)

            if len(Cs) == M-1:
                flag = False
                break

    for i in stack:
        if i != [-1]:
            cheeze, last = i
            break
    print(Cs)
    print("#{} {}".format(test_case, last))















