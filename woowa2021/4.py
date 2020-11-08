from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(start, board, endNumber):
    start_x, start_y, count = start
    queue = deque([start])
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    visited[start_x][start_y] = 1
    while queue:
        x, y, count = queue.popleft()
        if board[x][y] == endNumber:
            return (x, y, 0), count + 1
        
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            if xx == -1:
                xx = n -1
            if xx == n:
                xx = 0
            if yy == -1:
                yy = n - 1
            if yy == n:
                yy = 0
            if visited[xx][yy]:
                continue
            visited[xx][yy] = 1
            queue.append((xx, yy, count + 1))
def solution(n, board):
    answer = 0
    start = (0, 0, 0)
    for i in range(1, n * n + 1):
        new_start, count = BFS(start, board, i)
        answer += count
        start = new_start
    print(answer)
    return answer



solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]])
solution(2, [[2, 3], [4, 1]])
solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]])
