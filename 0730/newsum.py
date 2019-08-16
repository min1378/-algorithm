
matrix = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# for i in range(5) :
#     temp=[]
#     for j in range(5):
#         temp.append(randint(1,25))
#     matrix.append(temp)
def isWall(x, y) :
    if x < 0 or x >= 5 : 
        return True
    if y < 0 or y >= 5 :
        return True
    return False
def calAbs(x, y) :
    if x - y > 0 :
        return x - y
    if x - y < 0 :
        return y - x
sum_1 = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])) :
        testX1 = 0
        testX2 = 0
        testY1 = 0
        testY2 = 0
        for Mode in range(4) :
            testX = x + dx[Mode]
            testY = y + dy[Mode]
            if isWall(testX, testY) == False:
                sum += calAbs(matrix[x][y], matrix[testX][testY])

print(sum_1)
