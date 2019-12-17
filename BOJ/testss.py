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

import heapq
import sys
# sys.stdin = open('t.txt', 'r')
# 입력
V, E = map(int, input().split())
K = 1
INF = 10 * V + 1  # 최댓값 설정
distance = [[] for _ in range(V + 1)]  # V*V배열로 만들면 메모리가 초과된다

for _ in range(E):
    start, end, dist = map(int, sys.stdin.readline().split())
    distance[start].append([end, dist])  # 시작 리스트에 도착지와 거리를 입력

# 다익스트라 알고리즘
queue = []  # 우선순위 큐 -> 힙으로 구현해줌
K_distance = [INF for _ in range(V + 1)]  # 답이 될 K로부터의 거리
K_distance[K] = 0  # 자기 자신은 0
heapq.heappush(queue, [0, K])  # 자기 자신으로부터 우선순위 큐를 시작한다

while queue:
    mid = heapq.heappop(queue)  # 현재 가장 가까운 거리의 노드를 pop [거리, 노드 위치]
    for end in distance[mid[1]]:  # 가장 가까운 노드에 연결된 모든 노드들 end에 대하여
        if K_distance[end[0]] > mid[0] + end[1]:  # mid노드를 거치는 게 end로 바로 가는 것보다 효율적이라면
            K_distance[end[0]] = mid[0] + end[1]  # 해당 거리를 저장
            heapq.heappush(queue, [K_distance[end[0]], end[0]])  # 큐에 [갱신된 거리, 노드 위치] 삽입

# 출력
print(K_distance[-1])