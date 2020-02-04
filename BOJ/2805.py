import sys
sys.stdin = open('i2805.txt', 'r')
input = sys.stdin.readline
def solve():
    global M
    left = 0
    right = data[-1]
    
    while left <= right:
        mid = (left + right) // 2
        
        result = 0
        print(left, right, mid)
        if left == right:
            return mid
        for i in range(N-1, -1, -1):
            print("data", i, data[i])
            if data[i] < mid :
                break
            result += data[i] - mid
        print("result", result)
        if result < M:
            right = mid - 1
        elif result > M:
            left = mid + 1
        else:
            return mid
N, M = map(int, input().split())
data = list(map(int, (input().split())))
data.sort()
print(solve())