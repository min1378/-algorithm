import sys

sys.stdin = open('5102.txt')

TC = int(input())
for test_case in range(1, TC+1):
    V, E = map(int, input().split())
    data = []
    for i in range(E):
        temp = list(map(int, input().split()))
        data.append(temp)


    start, end = map(int, input().split())

# 딕셔너리로 연결
    dic = {}

    for E_start, E_end in data:
        if dic.get(E_start) :
            dic[E_start].append(E_end)
        if dic.get(E_end) :
            dic[E_end].append(E_start)
        if not dic.get(E_start):
            dic[E_start] = [E_end]
        if not dic.get(E_end):
            dic[E_end] = [E_start]

    print(dic)
    stack = []
    count = 0
    # visited 행렬 생성
    visited = [False] * (V+1)
    visited[0] = True


    while True:
        # start와 end가 같다면 도착한 것이니 탈출
        if start == end:
            break
        # visited 에 True 체크
        visited[start] = True

        if start in dic.keys():
            for v in dic[start]:
                if visited[v] == False:
                    stack.append([v, count])


        if stack == []:
            break

        start, count = stack.pop(0)

        if not False in visited:
            count = 0
            break

        count += 1
    print("#{} {}".format(test_case, count))