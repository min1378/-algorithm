import sys
sys.stdin = open("input.txt", "r")
              
T = 10
for test_case in range(1, T + 1):
    V, E = map(int,input().split())
    temp = list(map(int, input().split()))
    info = []
    # data (V+1) X (V+1)빈 행렬을 만든다.
    data= [[0] * (V + 1) for _i in range(V + 1)]
    # data 행렬에 간선 데이터를 입력 1 => 연결되어 있음.
    for i in range(len(temp)):
        if i % 2 == 0 :
            data[temp[i+1]][temp[i]] = 1 

    # ended 행렬을 만들어 체크한다. ()              
    ended = [False] * len(data)
    # 0번째는 True로 초기화 (안쓰임)
    ended[0] = True

    stack = []
    #시작값은 입력받은 데이터의 첫째값으로 한다.
    i = temp[0]
    result = ''
    while True :
        # 스택이 입력되었는지 카운트(0 / 1) 한다.
        count = False 
        # ended[i] == False 라면 끝나지 않았으니 실행!       
        if ended[i] == False :
            #만약에 data[i] 에 1이란 값이 있다면 체크를한다.. 너무오래걸려서 추가함.
            if 1 in data[i]:
                # i값을 고정하고 j를 돌아 1인 데이터가 있는지 확인! 있으면 스택에 추가. 그리고 카운트를 1로 변경.
                for j in range(1, len(data)):           
                    if data[i][j] == 1:
                        stack.append(j)
                        count = True
            # append하지 않았다면 0차수라는 뜻이기 때문에 i를 종결시키고 결과값에 집어넣는다.
            if count == False :
                ended[i] = True
                result += str(i) + ' '
                # 그리고 반복문을 돌아 1인 값을 찾고 스택에 집어넣는다.  그리고 data를 0으로 변경
                for j in range(len(data)):
                    if data[j][i] == 1:
                        stack.append(j)
                        data[j][i] = 0
        # 만약에 stack이 비어 있고 ended에 False(아직 끝나지 않았다면) 라면 false인 인덱스를 찾아 i값에 집어넣는다.
        if stack == [] and False in ended :
            for f in range(len(ended)):
                if ended[f] == False:
                    i = f
                    break
        # stack값이 비어 있지 않다면 stack의 마지막 부분을 꺼내 i에 집어넣는다.       
        if stack != [] : 
            i = stack.pop()
        # ended가 전부 True 라면 while문을 탈출한다.
        if False not in ended :
            break

            
    print('#{} {}'.format(test_case, result))

