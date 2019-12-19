# import sys
# #sys.stdin = open('t.txt', 'r')
# def dijkstra(K, V, graph):
#     INF = sys.maxsize
#     # s는 해당 노드를 방문 했는지 여부를 저장하는 변수이다
#     s = [False] * V
#     # d는 memoization을 위한 array이다. d[i]는 정점 K에서 i까지 가는 최소한의 거리가 저장되어 있다.
#     d = [INF] * V
#     d[K - 1] = 0
#
#     while True:
#         m = INF
#         N = -1
#
#         # 방문하지 않은 노드 중 d값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
#         # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
#         for j in range(V):
#             if not s[j] and m > d[j]:
#                 m = d[j]
#                 N = j
#
#         # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
#         # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미이므로 반복문을 빠져나간다.
#         if m == INF:
#             break
#
#         # N번 노드를 '방문'한다.
#         # '방문'한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는 노드가 있는지 확인하고,
#         # 더 빨리 갈 수 있다면 해당 노드(노드의 번호 j라고 하자)의 d[j]를 업데이트 해준다.
#         s[N] = True
#
#         for j in range(V):
#             if s[j]: continue
#             via = d[N] + graph[N][j]
#             if d[j] > via:
#                 d[j] = via
#
#     return d[-1]
# N, M = map(int, input().split())
# INF = sys.maxsize
# graph = [[INF]*N for _ in range(N)]
#
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     graph[u-1][v-1] = w
# start = 1
# end = N
# print(dijkstra(start, N, graph))

# import heapq
# import sys
# #sys.stdin = open('t.txt', 'r')
# # 입력
# V, E = map(int, input().split())
# K = 1
# INF = sys.maxsize  # 최댓값 설정
# distance = {i: [] for i in range(V + 1)}  # V*V배열로 만들면 메모리가 초과된다
#
# for _ in range(E):
#     start, end, dist = map(int, input().split())
#     distance[start].append([end, dist])  # 시작 리스트에 도착지와 거리를 입력
#
# # 다익스트라 알고리즘
# queue = []  # 우선순위 큐 -> 힙으로 구현해줌
# K_distance = [INF for _ in range(V + 1)]  # 답이 될 K로부터의 거리
# K_distance[K] = 0  # 자기 자신은 0
# heapq.heappush(queue, (0, K))  # 자기 자신으로부터 우선순위 큐를 시작한다
#
# while queue:
#     mid = heapq.heappop(queue) # 현재 가장 가까운 거리의 노드를 pop [거리, 노드 위치]
#     if K_distance[mid[1]] < mid[0]:
#         continue
#
#     for end in distance[mid[1]]:  # 가장 가까운 노드에 연결된 모든 노드들 end에 대하여
#         if K_distance[end[0]] > mid[0] + end[1]:  # mid노드를 거치는 게 end로 바로 가는 것보다 효율적이라면
#             K_distance[end[0]] = mid[0] + end[1]  # 해당 거리를 저장
#             heapq.heappush(queue, (K_distance[end[0]], end[0]))  # 큐에 [갱신된 거리, 노드 위치] 삽입
#
# print(K_distance[V])

#
# import sys
# import heapq
# #sys.stdin = open('t.txt', 'r')
# input = sys.stdin.readline
# INF = sys.maxsize
# V, E = map(int, input().split())
# #시작점 K
# K = 1
# #가중치 테이블 dp
# dp = [INF]*(V+1)
# heap = []
# graph = [[] for _ in range(V + 1)]
# def Dijkstra(start):
#     #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
#     dp[start] = 0
#     heapq.heappush(heap,(0, start))
#
#     #힙에 원소가 없을 때 까지 반복.
#     while heap:
#         wei, now = heapq.heappop(heap)
#         #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
#         if dp[now] < wei:
#             continue
#         if now == V:
#             return wei
#         for w, next_node in graph[now]:
#             #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
#             # = 다음 노드까지의 가중치(next_wei)
#             next_wei = w + wei
#             #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
#             if next_wei < dp[next_node]:
#                 #계산했던 next_wei를 가중치 테이블에 업데이트.
#                 dp[next_node] = next_wei
#                 #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
#                 heapq.heappush(heap, (next_wei, next_node))
#
# #초기화
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     #(가중치, 목적지 노드) 형태로 저장
#     graph[u].append((w, v))
#
#
# print(Dijkstra(K))


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and not visited[node]:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def Dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        if graph.get(node):
            neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        visited[node] = 1
        node = find_lowest_cost_node(costs)

import sys
#sys.stdin = open('t.txt', 'r')
infinity = float("inf")
graph = {}
K = 1
input = sys.stdin.readline
V, E = map(int, input().split())
costs = {i:infinity for i in range(1, V+1)}

costs[K] = 0
parents = {}
visited = [0] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    if graph.get(u) == None:
        graph[u] = {}
    graph[u][v] = w
    parents[v] = u

Dijkstra()
print(costs[V])