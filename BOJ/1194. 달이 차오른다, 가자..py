import sys
sys.stdin = open('1194.txt', 'r')


from collections import deque

def isWall(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return True
    if data[x][y] == '#':
        return True
    return False

def key_update(key, letter):

    if letter == 'a':
        key = (key | 1)
    elif letter == 'b':
        key = (key | 2)
    elif letter == 'c':
        key = (key | 4)
    elif letter == 'd':
        key = (key | 8)
    elif letter == 'e':
        key = (key | 16)
    elif letter == 'f':
        key = (key | 32)
    return key

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, count, key):
    global min_count
    queue = deque([(x, y, count, key)])
    while queue:
        x, y, count, key = queue.popleft()
        if data[x][y] == '1':
            min_count = count
            return

        if ord('a') <= ord(data[x][y]) <= ord('f'):
            key = key_update(key, data[x][y])
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if isWall(xx, yy):
                continue
            if visited[xx][yy][key]:
                continue
            if ord("A") <= ord(data[xx][yy]) <= ord("F"):
                temp = ord(data[xx][yy]) - ord("A")
                if key & (1 << temp) <= 0:
                    continue
                visited[xx][yy][key] = True
                queue.append((xx, yy, count + 1, key))
            else:
                visited[xx][yy][key] = True
                queue.append((xx, yy, count + 1, key))



# TC = int(input())
# for test_case in range(1, TC+1):

min_count = -1
N, M = map(int, input().split())
data = [input() for _ in range(N)]
visited = [[[0 for depth in range(1 << 6)] for col in range(M)] for row in range(N)]
for i in range(N):
    for j in range(M):
        if data[i][j] == '0':
            BFS(i, j, 0, 0)
print(min_count)



