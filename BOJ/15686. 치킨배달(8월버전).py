import sys
sys.stdin = open('15686.txt', 'r')

from itertools import combinations
N, M = map(int, input().split())
mapdata = [list(map(int, input().split())) for _ in range(N)]


chicken = []
home = []
for i in range(N):
    for j in range(N):
        if mapdata[i][j] == 2:
            chicken.append([i, j])
        elif mapdata[i][j] == 1:
            home.append([i, j])
dist = [[ 0 ] * len (home) for _ in range(len(chicken))]

for i in range(len(chicken)):
    for j in range(len(home)):
        dist[i][j] = abs(chicken[i][0] - home[j][0]) + abs(chicken[i][1] - home[j][1])

ans = 1e9



for info in combinations([i for i in range(len(chicken))], M):
    tsum = 0
    for h in range(len(home)):
        tmin = 1e9
        for cc in info:
            tmin = min(tmin, dist[cc][h])
        tsum += tmin
    ans = min(ans, tsum)

print(ans)