import sys
sys.stdin = open('11403.txt', 'r')
from collections import deque
TC = 2
def solve(start_x , start_y):
    queue = deque([(start_x, start_y)])

    while queue:
        # print(queue)
        # for line in result:
        #     print(line)
        # print("===========")
        x, y = queue.popleft()
        if result[start_x][y]:
            continue
        result[start_x][y] = 1
        for i in range(N):
            if data[y][i] :
                queue.append((y, i))


#for test_case in range(1, TC+1):
N = int(input())
data = [list(map(int ,input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j]:
            solve(i, j)
for line in result:
    print(' '.join(map(str, line)))