import sys
sys.stdin = open('3190.txt', 'r')
# TC = int(input())
def isWall(x, y):
    if x < 0 or x > N - 1:
        return True
    if y < 0 or y > N - 1:
        return True
    return False
def move(x, y):
    snake_location = [[x, y]]
    count = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    mode = 1
    i = 0
    while True:
        count += 1
        Test_X = x + dx[mode]
        Test_Y = y + dy[mode]
        if isWall(Test_X, Test_Y):
            return count
        if [Test_X, Test_Y] in snake_location:
            return count
        if data[Test_X][Test_Y]:
            snake_location.append([Test_X, Test_Y])
            data[Test_X][Test_Y] = 0
        elif data[Test_X][Test_Y] == 0:
            snake_location.append([Test_X, Test_Y])
            snake_location.pop(0)
        x = Test_X
        y = Test_Y
        if L > i:
            if count == int(change_info[i][0]):
                if change_info[i][1] == 'L':
                    if mode == 0:
                        mode = 3
                    else:
                        mode -= 1

                elif change_info[i][1] == 'D':
                    if mode == 3:
                        mode = 0
                    else:
                        mode += 1

                i += 1

#for test_case in range(1, TC+1):
N = int(input())
K = int(input())
data = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    data[x-1][y-1] = 1

L = int(input())
change_info = [0] * L
for i in range(L):
    change_info[i] = list(map(str, input().split()))


result = move(0, 0)
print(result)


#

