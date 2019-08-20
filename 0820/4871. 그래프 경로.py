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

    VE = list(map(int, input().split()))
    V = VE[0]
    E = VE[1]
    temp1 = []

    for i in range(E):
        temp1.append(list(map(int,(input().split())))) 
    temp2 = list(map(int,(input().split())))

    start = temp2[0]
    end = temp2[1]

    data = []

    for i in range(V+1):
        temp =[]
        for j in range(V+1):
            temp.append(0)
        data.append(temp)
    for i in range(len(temp1)):
        data[temp1[i][0]][temp1[i][1]] = 1
    
    result = search(data, start, end)
    print('#{} {}'.format(test_case, result))