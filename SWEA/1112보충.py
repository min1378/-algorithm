def BFS(v):
    q = []
    q.append(v)
    while q :
        v = q.pop(0)
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for w in G[v]:
                if not visited[w]:
                    q.append(w)


visited=[False] * (N+1)
G = [[], [2, 3]]