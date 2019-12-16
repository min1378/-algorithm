def push(s, x):
    s.append(x)


data = []
for i in range(8):
    temp = []
    for j in range(8):
        temp.append(0)
    data.append(temp)


data[1][2] = 1
data[1][3] = 1
data[2][1] = 1
data[2][5] = 1
data[2][4] = 1
data[3][1] = 1
data[3][7] = 1
data[4][2] = 1
data[4][6] = 1
data[5][2] = 1
data[5][6] = 1
data[6][4] = 1
data[6][5] = 1
data[7][3] = 1
data[7][6] = 1
visited = [False] * len(data)
visited[0] = True
stack = []
i = 2
result = ''
while True :
    if visited[i] == False :
        for j in range(1, len(data)):
            if data[i][j] == 1:
                push(stack, j)
        visited[i] = True
        result += str(i) + ' '
    i = stack.pop()
    if False not in visited:
        break

print(result)

        



