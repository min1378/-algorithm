import sys
import heapq
#sys.stdin = open('g.txt', 'r')
def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    return False
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def Dijkstra(start, x, y):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[x][y] = start
    heapq.heappush(heap,(start, x, y))

    #힙에 원소가 없을 때 까지 반복.
    while heap:

        wei, xx, yy = heapq.heappop(heap)
        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if xx == x2 and yy == y2:
            return print(wei)
        if dp[xx][yy] < wei:
            continue
        for mode in range(4):
            xxx = xx + dx[mode]
            yyy = yy + dy[mode]
            if isWall(xxx, yyy):
                continue

            next_wei = data[xxx][yyy] + wei
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if next_wei < dp[xxx][yyy]:
                #계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[xxx][yyy] = next_wei
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                heapq.heappush(heap, (next_wei, xxx, yyy))
    return wei
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int,input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    #가중치 테이블 dp
    dp = [[INF]*(M+1) for _ in range(N+1)]
    heap = []

    Dijkstra(data[x1][y1], x1, y1)