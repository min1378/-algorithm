import sys
sys.stdin = open('15685.txt', 'r')

def check(x, y):
    if data[x][y] and data[x+1][y] and data[x][y+1] and data[x+1][y+1]:
        return True
    return False
N = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
data =[[0] * 101 for _ in range(101)]



for _ in range(N):
    y, x, mode, g = map(int,input().split())
    data[x][y] = 1
    stack = [mode]

    for _ in range(g):
        for i in range(len(stack) -1, -1, -1):
            stack.append((stack[i] + 1) % 4)

    for i in range(2 ** g):

        xx = x + dx[stack[i]]
        yy = y + dy[stack[i]]
        data[xx][yy] = 1
        x = xx
        y = yy
count = 0

for i in range(100):
    for j in range(100):
        if data[i][j]:
            if check(i, j):
                count += 1

print(count)