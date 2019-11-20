import sys
sys.stdin = open('1260.txt', 'r')
TC = int(input())
def DFS(dic,start):
    for value in dic.values():
        value.reverse()
    stack = dic[start]
    result_DFS = str(start) + ' '
    visited_DFS[start] = True
    while stack != [] :
        if False not in visited_DFS:
            break
        check = stack.pop()
        if visited_DFS[check] == False:
            result_DFS += str(check) + ' '
            stack.extend(dic[check])
            visited_DFS[check] = True

    return result_DFS
def BFS(dic,start):
    queue = dic[start]
    result_BFS = str(start) + ' '
    visited_BFS[start] = True
    while queue != [] :
        if False not in visited_BFS:
            break
        check = queue.pop(0)
        if visited_BFS[check] == False:
            result_BFS += str(check) + ' '
            queue.extend(dic[check])
            visited_BFS[check] = True

    return result_BFS
for test_case in range(1, TC+1):
    N, M, start = map(int, input().split())
    dic = {}
    for _ in range(M):
        temp = list(map(int, input().split()))
        if temp[0] in dic.keys():
            dic[temp[0]].append(temp[1])
            if temp[1] in dic.keys():
                dic[temp[1]].append(temp[0])
            else:
                dic[temp[1]] = [temp[0]]

        else:
            dic[temp[0]] = [temp[1]]
            if temp[1] in dic.keys():
                dic[temp[1]].append(temp[0])
            else:
                dic[temp[1]] = [temp[0]]

    visited_DFS = [False] * (N + 1)
    visited_DFS[0] = True
    visited_BFS = [False] * (N + 1)
    visited_BFS[0] = True
    for value in dic.values():
        value.sort()

    result_BFS = BFS(dic, start)
    result_DFS = DFS(dic, start)


    print(result_DFS)
    print(result_BFS)