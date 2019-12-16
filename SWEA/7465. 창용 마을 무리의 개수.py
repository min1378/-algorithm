import sys
sys.stdin = open('7465.txt', 'r')

def check_union():
    global count
    for i in range(1, N+1):
        stack = []
        if visited[i] == False:
            stack.append(i)
        check = False
        while stack != []:
            check = True
            go = stack.pop()
            if visited[go] == 0:
                stack += dic[go]
                visited[go] = True
        if check == True:
            count += 1
TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    dic = {i : [] for i in range(1, N+1)}
    for _ in range(M):
        temp = list(map(int, input().split()))
        dic[temp[0]].append(temp[1])
        dic[temp[1]].append(temp[0])
    visited = [0] * (N+1)
    count = 0
    check_union()
    print("#{} {}".format(test_case, count))

