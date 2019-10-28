import sys
sys.stdin = open('5248.txt', 'r')
TC = int(input())
def BFS():
    global result
    for i in range(1, N+1):
        go = i
        flag = False
        if visited[go] == False and go in dic:
            for values in dic[go]:
                if visited[values] == False:
                    visited[values] = True
                    flag = True
        if flag == False:
            result += 1
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    info = list(map(int, input().split()))
    dic = {}
    visited = [False] *(N + 1)
    for i in range(M*2):
        if i % 2 == 0:
            if info[i] in dic:
                dic[info[i]].append(info[i+1])

            if info[i+1] in dic:
                dic[info[i+1]].append(info[i])
            if info[i] not in dic:
                dic[info[i]] = [info[i+1]]

            if info[i+1] not in dic:
                dic[info[i+1]] = [info[i]]
    result = 0
    print(dic)
    BFS()
    print(N - result)


