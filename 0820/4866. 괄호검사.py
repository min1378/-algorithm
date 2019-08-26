import sys
sys.stdin = open("input.txt", "r")
# 리스트안에 담긴 괄호를 검사하는 inspect 함수
def inspect(temp) :
    stack = []
    # temp 리스트를 확인한다.
    for i in temp :
        # 
        if stack != [] and stack[-1] == '(' and i == ')' :
            stack.pop()
        elif stack != [] and stack[-1] == '{' and i == '}' :
            stack.pop()
        elif i == '(' or i == ')' or  i == '{' or  i == '}' :
            stack.append(i)

    if stack == [] :
        return 1    
    else :
        return 0
T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(str, input()))
    result = inspect(temp)   
    print('#{} {}'.format(test_case, result))