import sys
sys.stdin = open('4866.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    data = input()
    mystack = []
    for i in range(len(data)):
        # 짝이 맞는지만 검사
        if data[i] == "(" or data[i] == "{":
            mystack.append(data[i])
        elif data[i] == ")" or data[i] == "}":
            if len(mystack) == 0:
                mystack.append(data[i])  # 잘못된 문장
                break # 잘못된 경우 발견시 종료
            elif (data[i] == ")" and mystack[-1] != "(") or (data[i] == "}" and mystack[-1] != "{"):
                mystack.append(data[i])  # 잘못된 문장
                break
            else:
                mystack.pop()
    #문장검사 종료
    if len(mystack) == 0 :
        print("#%s %s" % (tc, 1)) # 바른 문장일 경우 
    else :
        print("#%s %s" % (tc, 0)) # 틀린 문장일 경우


