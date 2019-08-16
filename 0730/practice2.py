

def isWall(x, y) :
    if x < 0 or x >= 5 : 
        return True
    if y < 0 or y >= 5 :
        return True
    return False
a = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21], 
[8, 24, 10, 17, 7], 
[15, 4, 16, 5, 6], 
[12, 13, 22, 23, 14]]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for x in range(len(matrix)):
    for y in range(len(matrix[x])) :
        for Mode in range(4) :
            testX = x + dx[Mode]
            testY = y + dy[Mode]
            if isWall(testX, testY) == False:
                sum += calAbs(matrix[x][y], matrix[testX][testY])










def selectionSort(a) :
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j] :
                min = j
                a[i], a[min] = a[min], a[i]
    print(a)

print(selectionSort(a))
