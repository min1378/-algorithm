import sys
sys.stdin = open('input.txt', 'r')
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def DFS():
    stack = [(0, 0, data[0][0])]
    count = 0
    while stack:
        x, y, path = stack.pop()
        flag = True
        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > R - 1 or yy < 0 or yy > C - 1:
                continue
            if data[xx][yy] in path:
                continue
            if visited[xx][yy] != path + data[xx][yy]:
                flag = False
                visited[xx][yy] = path + data[xx][yy]
                stack.append((xx, yy, path + data[xx][yy]))
    
        if flag:
            count = max(count, len(path))
    return count


R, C = map(int, input().strip().split())

data = [list(input().strip()) for _ in range(R)]
visited = [[''] * C for _ in range(R)]
print(DFS())

