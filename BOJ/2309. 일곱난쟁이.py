import sys
sys.stdin = open('input1.txt', 'r')
def solve(start, list):
    global flag
    if flag:
        return
    if sum(list) > 100:
        return
    if len(list)==7:

        result = 0
        for el in list:
            result += nine[el]

        if result == 100:
            flag = True
            seven = []
            for el in list:
                seven.append(nine[el])
            seven.sort()
            for ell in seven:
                print(ell)
        return
    for i in range(start, 9):
        if visited[i]:
            continue
        visited[i] = 1
        solve(i+1, list + [i])
        visited[i] = 0
nine = []
visited = [0] * 9
for _ in range(9):
    temp = int(input())
    nine.append(temp)
flag = False
solve(0, [])
# 0 1 2 3 4 5 6
# 0 2 3 4 5 6 7
# 0 3 4 5 6 7 8
# 1 2 3 4 5 6 7
# 1 3 4 5 6 7 8
# 2 3 4 5 6 7 8

