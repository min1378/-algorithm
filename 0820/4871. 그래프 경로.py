import sys
sys.stdin = open("input.txt", "r")

def search(data, start, end):
    i = start
    stack = []
    visited = [False] * len(data)
    visited[0] = True
    while True :
        if i == end :
            return 1
        if stack == [] and 1 not in data[i]:
            return 0
        if visited[i] == False :
            if 1 in data[i] :
                for j in range(1, len(data)):
                    if data[i][j] == 1:
                        stack.append(j)
            elif 1 not in data[i]: 
                visited[i] = True         
        i = stack.pop()

T = int(input())
for test_case in range(1, T + 1):

    V, E = map(int, input().split())
    data = []

    for i in range(E):
        start_node, end_node = map(int, input().split())
        data[start_node][end_node] = 1
    start, end = map(int, input().split())

    result = search(data, start, end)
    print('#{} {}'.format(test_case, result))