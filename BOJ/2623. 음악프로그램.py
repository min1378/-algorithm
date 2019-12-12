import sys
sys.stdin = open('2623.txt', 'r')
from collections import deque
N, M = map(int, input().split())
dic = {}
vertex_visited_count = [0] * (N+1)
vertex_visited_count[0] = -1
for _ in range(M):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-1):
        if dic.get(temp[i]):
            dic[temp[i]].append(temp[i+1])
            vertex_visited_count[temp[i+1]] += 1
        else:
            dic[temp[i]] = [temp[i+1]]
            vertex_visited_count[temp[i+1]] += 1

queue = deque([])
for i in range(1, len(vertex_visited_count)):
    if vertex_visited_count[i] == 0:
        queue.append(i)
result = []
vertex_count = 0
while queue:
    start = queue.popleft()
    result.append(start)
    vertex_count += 1
    if dic.get(start):
        for element in dic[start]:
            vertex_visited_count[element] -= 1
            if vertex_visited_count[element] == 0:
                queue.append(element)

if vertex_count != N:
    result = 0
    print(result)
else:
    for i in result:
        print(i)