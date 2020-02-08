from copy import deepcopy
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = 5
M = 5
def connect_check(check):
    visited = [0] * len(check)
    check2 = [check[0]]
    while check2:
        x, y = check2.pop()
        print(visited)
        for a, b in direction:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > N - 1 or yy < 0 or yy > M - 1:
                continue
            if (xx, yy) not in check:
                continue
            index = check.index((xx, yy))
            if visited[index]:
                continue
            visited[index] = 1
            check2.append((xx, yy))
    if sum(visited) == 4:
        return True
    else:
        return False
#[6, 7, 16, 17] [(1, 0), (1, 1), (3, 0), (3, 1)]
print(connect_check([(1, 0), (1, 1), (3, 0), (3, 1)]))