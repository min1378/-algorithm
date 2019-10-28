import sys
sys.stdin = open('5521.txt', 'r')
TC = int(input())
for t in range(1, TC + 1):
    node, edge = map(int, input().split())

    edges = []
    for e in range(edge):
        edges.extend(map(int, input().split()))
    # print(edges)

    g = [[0] * (node + 1) for i in range(node + 1)]
    for i in range(0, len(edges), 2):
        g[edges[i]][edges[i + 1]] = 1
        g[edges[i + 1]][edges[i]] = 1
    # print(g)
    res = [0] * (node + 1)

    # print(g[1])  # 상원이 친구
    for i in range(2, node + 1):
        for j in range(2, node + 1):
            if g[1][i] and g[i][j]:
                res[j] = 1
    print(res)

    # 1,1 은 상원이 지니까 0으로 만들어주기
    res[1] = 0
    print('#{} {}'.format(t, sum(res)))
