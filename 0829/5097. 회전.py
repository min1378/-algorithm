import sys
sys.stdin = open('5097.txt', 'r')


TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    stack = list(map(int, input().split()))

    for i in range(M):
        temp = stack.pop(0)
        stack.append(temp)

    print("#{} {}".format(test_case, stack[0]))