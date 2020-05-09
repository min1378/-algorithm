data = [[0] * 6 for _ in range(6)]

def DFS(start_x, start_y):
    global data
    visited = [[0] * 6 for _ in range(6)]
    check = [[start_x, start_y]]
    stack = [[start_x, start_y]]
    color = data[start_x][start_y]
    visited[start_x][start_y] = 1
    while stack:
        x, y = stack.pop()
        for a, b in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            xx = x + a
            yy = y + b
            if xx < 0 or xx > 5 or yy < 0 or yy > 5:
                continue
            if visited[xx][yy]:
                continue
            visited[xx][yy] = 1
            if data[xx][yy] == color:
                check.append([xx,yy])
                stack.append([xx,yy])
    return check

def see(data):
    for line in data:
        print(line)
    print("================")
def ans(data):
    answer = []
    for line in data:
        temp = ""
        for el in line:
            temp += str(el)
        answer.append(temp)
    return answer

def putmaca(y, color):
    global data
    for x in range(6):
        if data[x][y] != 0:
            data[x-1][y] = color
            return x - 1
    data[5][y] = color
    return 5

def downmaca(y, color):
    global data
    for x in range(5, -1, -1):
        if data[x][y] != 0:
            continue
        data[x][y] = color
        return x
def search(deletes):
    count = [0, 0, 0, 0, 0, 0]
    for delete in deletes:
        x = delete[0]
        y = delete[1]
        data[x][y] = 0
        count[y] = 1
    for y in range(len(count)):
        if count[y] == 0:
            continue
        for x in range(4, -1, -1):
            if data[x][y] == 0:
                continue
            color = data[x][y]
            data[x][y] = 0
            downmaca(y, color)   
def solution(macaron):
    
    global data
    for maca in macaron:
        
        y = maca[0] - 1
        color = maca[1]
        x = putmaca(y, color)
        deletes = DFS(x, y)
        if len(deletes) > 2:
            search(deletes)
            for aa in range(6):
                for bb in range(6):
                    if data[aa][bb] > 0:
                        temp_deletes = DFS(aa, bb)
                        if len(temp_deletes) > 2:
                            search(temp_deletes)
    answer = ans(data)
    return answer






# print(solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])) # [000000,000000,000000,000000,000000,204004]
print(solution([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]))