import sys
sys.stdin = open('16236.txt', 'r')
TC=int(input())
from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def isWall(x, y):
    if x < 0 or x > N - 1:
        return True
    if y < 0 or y > N - 1 :
        return True
    return False

def BFS(x, y):
    queue = deque([[x, y, 0]])
    visited = [[False] * N for _ in range(N)]
    feed = []
    min_count = N ** 2
    while queue:
        temp = queue.popleft()
        xx = temp[0]
        yy = temp[1]
        count = temp[2]

        if min_count < count :
            return feed
        visited[xx][yy] = True
        count += 1
        for mode in range(4):
            Test_x = xx + dx[mode]
            Test_y = yy + dy[mode]
            if isWall(Test_x, Test_y) == False:
                if visited[Test_x][Test_y] == False:
                    visited[Test_x][Test_y] = True
                    if baby_info[0] >= data[Test_x][Test_y]:
                        queue.append([Test_x, Test_y, count])
                    if 0 < data[Test_x][Test_y] < baby_info[0]:
                        if min_count >= count:
                            feed.append([Test_x, Test_y, count])
                            min_count = count

    if feed:
        return feed
    return False
def move(baby):
    global count
    baby_size = baby[0]
    x = baby[1]
    y = baby[2]
    baby_ex = baby[3]

    feed = BFS(x, y)
    if feed == False:
        return False

    if len(feed) > 1:
        min_high = 20
        min_left = 20
        check = 0
        for i in range(len(feed)):
            if feed[i][0] < min_high:
                min_high = feed[i][0]
                min_left = feed[i][1]
                check = i
            elif feed[i][0] == min_high:
                if feed[i][1] < min_left:
                    min_left = feed[i][1]
                    check = i

        last = feed[check]
    else:
        last = feed[0]

    baby_ex += 1
    if baby_ex == baby_size:
        baby_ex = 0
        baby_size += 1

    baby_info[0] = baby_size
    baby_info[1] = last[0]
    baby_info[2] = last[1]
    baby_info[3] = baby_ex
    count += last[2]
    data[last[0]][last[1]] = 0
    return True

#for test_case in range(1, TC+1):
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
baby_info = []
count = 0

for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            baby_info = [2, i, j, 0]
            data[i][j] = 0
result = True
while result:
    result = move(baby_info)

print(count)