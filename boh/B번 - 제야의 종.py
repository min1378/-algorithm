import sys
sys.stdin = open('b.txt', 'r')
def solve():
    check = [0] * N
    count = 0
    for i in range(M):
        count += 1
        for j in range(N):
            if data[j][i] == 1:
                if i != 0 and check[j] == 1:
                    continue

                check[j] = 1
            if data[j][i] == 0:
                if check[j] == 0:
                    continue

        for coun in check:
            if coun // count == 1 or coun == 0 :
                continue
            return print("NO")
    return print("YES")
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
solve()
