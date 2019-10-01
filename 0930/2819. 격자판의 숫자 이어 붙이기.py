import sys
sys.stdin = open('2819.txt', 'r')
TC = int(input())


def isWall(x, y):
    if x < 0 or x > 3 :
        return True
    if y < 0 or y > 3:
        return True
    return False

def permu(arr, i, j):
    if len(arr) == 7:
        result = ''
        for i in range(len(arr)):
            result += str(arr[i])
        if result not in answer:
            answer.append(result)
    dx = [-1, -0, 1, 0]
    dy = [0, 1, 0, -1]
    for mode in range(4):
        x = i + dx[mode]
        y = j + dy[mode]
        if isWall(x,y) == False:
            permu(arr + [data[x][y]], x, y)


for test_case in range(1, TC+1):
    data = [list(map(int, input().split())) for _ in range(4)]
    answer = []
    for i in range(4):
        for j in range(4):
            stack = []
            temp = [str(data[i][j])]
            permu([data[i][j]], i, j)
    print("#{} {}".format(test_case, len(answer)))