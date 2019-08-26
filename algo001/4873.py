import sys
sys.stdin = open('4873.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    data = list(input())
    n = len(data) #문자열 길이
    stack = [] # 지울 문자열들을 저장할 stack
    for i in range(n):
        # 스택이 비어있거나 스택 마지막 값이 현재 처리할 값과 다르면 저장
        if not stack or stack[-1] != data[i] :
            stack.append(data[i])
        elif stack and stack[-1] == data[i] :
            stack.pop() #stack의 마지막 글자 삭제

    print("%s %s" % (tc, len(stack)))