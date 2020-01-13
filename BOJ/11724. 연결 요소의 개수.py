import sys
#sys.stdin = open('11724.txt', 'r')
input = sys.stdin.readline
from collections import deque
def DFS(start):
    stack = [start]
    while stack:
        top = stack.pop()
        if dic.get(top):
            for el in dic[top]:
                if visited[el]:
                    continue
                visited[el] = 1
                stack.append(el)

    return
#for test_case in range(1, TC+1):
N, M = map(int, input().split())
dic = {}
for _ in range(M):
    v1, v2 = map(int, input().split())
    if dic.get(v1):
        dic[v1].append(v2)
    else:
        dic[v1] = [v2]

    if dic.get(v2):
        dic[v2].append(v1)
    else:
        dic[v2] = [v1]
visited = [0] * (N + 1)
visited[0] = 1
count = 0
for key in dic.keys():
    if visited[key]:
        continue
    DFS(key)
    count += 1

count += visited.count(0)

print(count)

