from collections import deque
# TC = int(input())
# for test_case in range(1, TC+1):
N, M, K = map(int, input().strip().split())
food = [list(map(int , input().strip().split())) for _ in range(N)]
data = [[5 for _ in range(N+1)] for _ in range(N+1)]
tree_info = deque([list(map(int, input().strip().split())) for _ in range(M)])
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    five_tree = []
    dead_tree = []
    # 봄
    for _ in range(len(tree_info)):
        x, y, age = tree_info.popleft()
        if data[x][y] >= age:
            data[x][y] -= age
            age += 1
            tree_info.append([x, y, age])
            if age % 5 == 0:
                five_tree.append([x, y, age])
        else:
            dead_tree.append([x, y, age])

    # 여름
    for i in range(len(dead_tree)):
        x, y, age = dead_tree[i]
        data[x][y] += age // 2

    # 가을
    for i in range(len(five_tree)):
        x = five_tree[i][0]
        y = five_tree[i][1]
        for mode in range(8):
            test_x = x + dx[mode]
            test_y = y + dy[mode]
            if (0 < test_x < N+1) and (0 < test_y < N+1):
                tree_info.appendleft([test_x, test_y, 1])

    # 겨울
    for i in range(1,N+1):
        for j in range(1,N+1):
            data[i][j] += food[i-1][j-1]

print(len(tree_info))