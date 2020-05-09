from collections import deque
dx = [-1, 0, 1 ,0]
dy = [0, 1, 0, -1]
answer = 55*10000
def isWall(x, y, n):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return True
    return False
def BFS(visited, deque, board):
    global answer
    while deque:
        x, y, direc, result = deque.popleft()
        if result >= answer:
            continue
        if x == len(board) - 1 and y == len(board) - 1:
            answer = min(answer, result)
            continue
        # print("(",x,",", y,")","방향:", direc,"금액", result)
        # for line in visited:
        #     print(line)
        for mode in range(4):
            xx = x + dx[mode]
            yy = y + dy[mode]
            new_direc = mode
            if isWall(xx, yy, len(board)):
                continue
            if board[xx][yy]:
                continue
            if new_direc != direc:
                new_result = result + 600
            else:
                new_result = result + 100
            if 0 < visited[xx][yy][0] <= new_result:
                continue
            
            visited[xx][yy][0] = new_result

            deque.append((xx, yy, new_direc, new_result))
def solution(board):
    global answer
    N = len(board)
    stack = []
    for mode in range(4):
        xx = 0 + dx[mode]
        yy = 0 + dy[mode]
        if isWall(xx, yy, len(board)):
            continue
        if board[xx][yy]:
            continue
        stack.append((xx, yy, mode, 100))
    for stac in stack:
        visited = [[[0 for depth in range(1 << 1)] for col in range(N)] for row in range(N)]
        visited[0][0][0] = 0
        visited[stac[0]][stac[1]][0] = 100
        BFS(visited, deque([stac]), board)

    return answer

print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))