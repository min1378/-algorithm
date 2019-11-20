import sys
sys.stdin = open('14889.txt', 'r')
TC = int(input())

def solve(k, s):
    global ans
    if k == R:
        start = link = 0

        x = list(set([x for x in range(N)]) - set(t))

        for i in range(R - 1):
            for j in range(i + 1, R):
                start += (data[t[i]][t[j]] + data[t[j]][t[i]])
                link += (data[x[i]][x[j]] + data[x[j]][x[i]])
        ans = min(ans, abs(start - link))
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = i
            solve(k + 1, i + 1)

#for test_case in range(1, TC+1):
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
R = N // 2
t = [0] * R
ans = 1e9
solve(0,0)
print(ans)