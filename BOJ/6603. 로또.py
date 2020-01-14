import sys
sys.stdin = open('6603.txt', 'r')

def comb(index, list):
    if len(list) == 6:
        print(" ".join(map(str, list)))
        return

    for i in range(index, K):
        if visited[i]:
            continue
        visited[i] = 1
        comb(i+1, list+[data[i]])
        visited[i] = 0

while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break

    K = temp[0]
    visited = [0] * K
    data = temp[1:]
    comb(0, [])
    print(" ")