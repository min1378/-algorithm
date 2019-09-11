import sys
sys.stdin = open('4881.txt', 'r')
# def f(row, score):
#     global min_sol
#
#     if row == N:
#         if score < min_sol:
#             min_sol = score
#         return min_sol
#
#     for i in range(N):
#         if visited[i] == False:
#             visited[i] = True
#             f(row+1, score + data[row][i])
#             visited[i] = False
#
#     return min_sol
#
# TC=int(input())
# for test_case in range(1, TC+1):
#     N = int(input())
#     data = []
#     for i in range(N):
#         temp = list(map(int, input().split()))
#         data.append(temp)
#     visited = [False] * N
#     min_sol = sys.maxsize
#     print(data)
#     result = f(0,0)
#     print(result)
TC=int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = []
    for i in range(N):
        temp = list(map(int, input().split()))
        data.append(temp)
    visited = [False] * N
    stack = []
    for i in range(N):
        stack.append([0,i,0])
    temp = 0
    min_sum = sys.maxsize
    while True:
        x, y, min_sum1 = stack.pop()
        visited[y] = True
        for i in range(N):
            if visited[i] == False:
                min_sum1 += data[x][y]
