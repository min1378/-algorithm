from collections import deque
def BFS(bigin):
    global count
    queue = deque([bigin])
    visited[bigin] = 1
    while queue:
        start = queue.popleft()
        count += 1
        if dic.get(start):
            for el in dic[start]:
                if visited[el]:
                    continue
                visited[el] = 1
                queue.append(el)


N = int(input())
M = int(input())
visited = [0] * (N+1)
count = 0
dic = {}
for _ in range(M):
    start, end = map(int, input().split())
    if dic.get(start):
        dic[start].append(end)
    else:
        dic[start] = [end]

    if dic.get(end):
        dic[end].append(start)
    else:
        dic[end] = [start]

BFS(1)
print(count)