import sys
sys.stdin = open("input.txt", "r")

def inspect(temp):
    stack = []
    for i in temp:
        if stack != [] and stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    return len(stack)
    
T = int(input())
for test_case in range(1, T + 1):
    temp = list(str(input()))
    result = inspect(temp)
    print('#{} {}'.format(test_case, result))