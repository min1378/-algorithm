import sys
sys.stdin = open('5521.txt', 'r')
TC = int(input())
def BFS(start):
    global result
    stack = [[start,0]]
    visited[start] = True
    while stack:

        x, count = stack[0]
        flag = False
        if count < 2 and x in dic:
            count += 1
            for value in dic[x]:

                if visited[value] == False:
                    print(value)
                    result += 1
                    flag = True
                    stack.append([value,count])

                    visited[value] = True

                    break

        if flag == False:
            stack.pop(0)

for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    dic = {}
    for _ in range(M):
        first, second = map(int, input().split())
        if first not in dic.keys():
            dic[first] = [second]

        if second not in dic.keys():
            dic[second] = [first]

        if first in dic.keys():
            dic[first].append(second)

        if second in dic.keys():
            dic[second].append(first)

    for key, value in dic.items():
        dic[key] = list(set(value))
    print(dic)
    visited = [False] * (N+1)
    result = 0
    BFS(1)
    print("#{} {}".format(test_case, result))