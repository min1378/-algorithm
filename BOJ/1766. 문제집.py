import sys
sys.stdin = open('1766.txt')
from collections import deque
N, M = map(int, input().split())
dic = {}
vertex_visited_count = [0] * (N+1)
vertex_visited_count[0] = -1
for _ in range(M):
    first, second = map(int, input().split())
    if dic.get(first):
        dic[first].append(second)
    else:
        dic[first] = [second]

queue = deque([])

for i in range(1, len(vertex_visited_count)):
    if vertex_visited_count[i] == 0:
        queue.append(i)

result = []
while queue:
    start = queue.popleft()
    if result == []:
        result.append(start)

    elif result:
        for i in range(len(result)):

    if dic.get(start):
        for el in dic[start]:
            vertex_visited_count[el] -= 1
            if vertex_visited_count[el] == 0:
                queue.append(el)
