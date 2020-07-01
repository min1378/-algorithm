D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# visited = []
macaron_map = []

def BFS(i, j, color):
    global macaron_map
    queue = [ (i, j) ]
    pos_list = [ (i, j) ]
    visited = [ [False] * 6 for _ in range(6) ]
    visited[i][j] = True
    while queue:
        que = queue.pop(0)
        y, x = que
        for k in range(4):
            idy = y + D[k][0]
            jdx = x + D[k][1]
            if 0 <= idy < 6 and 0 <= jdx < 6:
                if visited[idy][jdx] == False and macaron_map[idy][jdx] == color:
                    visited[idy][jdx] = True
                    queue.append((idy, jdx))
                    pos_list.append((idy, jdx))
    if len(pos_list) >= 3:
        # print('여기이이이')
        # 글로벌 조심 해보셈
        for pos in pos_list:
            yy, xx = pos
            macaron_map[yy][xx] = 0
        return True

def jaegui():
    global macaron_map
# 터뜨리는 과정
    for i in range(6):
        for j in range(6):
            if macaron_map[i][j] != 0:
                if BFS(i, j, macaron_map[i][j]) == True:
                    # print(*macaron_map, sep='\n')
                    # print('------------------------------')
                    # 내려보내는 과정
                    macaron_map2 = [ [0] * 6 for _ in range(6) ]
                    for j in range(6):
                        stack = []
                        for i in range(5, -1, -1):
                            if macaron_map[i][j] != 0:
                                stack.append(macaron_map[i][j])
                        for k in range(len(stack)):
                            macaron_map2[5 - k][j] = stack[k]
                    macaron_map = macaron_map2
                    # print('내려보낸 후')
                    # print(*macaron_map, sep='\n')
                    # print('------------------------------')
                    jaegui()

def solution(macaron):
    global macaron_map
    answer = []
    macaron_map = [ [0] * 6 for _ in range(6) ]
    for maca in macaron:
        x = maca[0] - 1
        color = maca[1]

        # 떨어뜨리는 과정
        for i in range(6):
            if i == 5:
                macaron_map[i][x] = color
            else:
                if macaron_map[i + 1][x] != 0:
                    macaron_map[i][x] = color
                    break

        
        jaegui()

        # print(*macaron_map, sep='\n')
        # print('------------------------------')

    # print(macaron_map)
    for m in macaron_map:
        answer.append(''.join(map(str, m)))

    return answer



solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])