import sys
sys.stdin = open('1697.txt', 'r')
TC = 3
from collections import deque

def isWall(x):
    if x < 0 or x > 100000:
        return True
    return False

def solve(start):
    count = 0
    queue = deque([(start, count)])
    visited[start] = 1
    while True:
        x, count = queue.popleft()

        if x == K:
            return count

        for mode in (x+1, x-1, x*2):
            xx = mode

            if isWall(xx):
                continue

            if visited[xx]:
                continue

            visited[xx] = 1
            queue.append((xx, count + 1))

#for test_case in range(1, TC+1):
N, K = map(int, input().split())
visited = [0] * 100001
print(solve(N))