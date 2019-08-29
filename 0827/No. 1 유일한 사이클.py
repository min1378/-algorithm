import sys
sys.stdin = open('1.txt', 'r')


TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())

    data = [[0]*(N+1) for i in range(N+1)]
    for _ in range(N):
        i, j = map(int, input().split())
        data[i][j] = 1

    count = 0




    for i in range(1, N):
        if count == N :
            break
        temp = 0
        visited = [False] * (N+1)
        for j in range(i):
            visited[j] = True
        start = i
        while True:
            if False not in visited and start != i:
                break
            if False not in visited and start == i:
                if count < temp:
                    count = temp
                break
            visited[i] = True
            for j in range(N+1):
                if data[i][j] == 1:
                    i = j
                    temp += 1
                    break
    print("#{} {}".format(test_case, count))