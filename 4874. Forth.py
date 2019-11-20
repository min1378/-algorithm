import sys
sys.stdin = open('4874.txt', 'r')
TC = int(input())

for test_case in range(1, TC+1):
    #수식 입력받기
    arithmetic = list(map(str, input().split()))
    
    # 입력받은 수식이 string값이므로 숫자는 int로 변환
    for j in range(len(arithmetic)) :
        i = arithmetic[j]
        if i == "+" or i == "-" or i == "/" or i == "*" or i == ".":
            continue
        arithmetic[j] = int(i)

    stack = []
    # 수식리스트의 개수만큼 반복문을 돈다.
    for j in range(len(arithmetic)):
        # result => 값을 저장
        result = 0
        i = arithmetic[j]
        # i가 int형이면 스택에 집어넣는다. 숫자이기 때문
        if type(i) == int :
            stack.append(i)
        # stack의 길이가 1개이상 즉 2개부터 연산을 처리한다.
        elif len(stack) > 1 and i == "+":
            # 들어가는 순서와 나오는 순서가 반대이기 때문에 pop시켜주면서 연산순서를 지정한다.
            back = stack.pop()
            front = stack.pop()
            result = front + back
            # 연산결과를 stack에 저장한다.
            stack.append(result)
        elif len(stack) > 1 and i == "-" :
            back = stack.pop()
            front = stack.pop()
            result = front - back
            stack.append(result)
        elif len(stack) > 1 and i == "/" :
            back = stack.pop()
            front = stack.pop()
            # 나눗셈 결과값은 float이기 때문에 int형으로 변환시켜준다.
            result = int(front / back)
            stack.append(result)
        elif len(stack) > 1 and i == "*":
            back = stack.pop()
            front = stack.pop()
            result = front * back
            stack.append(result)
        # .은 연산이 모두 끝나고 출력할때 처리하는 연산자이기 때문에 stack의 개수는 항상 1이어야한다.
        elif len(stack) == 1 and i == ".":
            result = stack.pop()
            break
        # 만약 위 조건을 모두 만족하지 못한다면 그것은 오류이기 때문에 result에 error 값을 넣고 반복문을 탈출한다.
        else :
            result = "error"
            break
    print("#{} {}".format(test_case, result))