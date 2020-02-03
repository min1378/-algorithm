import sys
sys.stdin = open('i2805.txt', 'r')
input = sys.stdin.readline
def solve():
    global M
    length = len(data)
    left = 0
    right = data[-1]
    
    while left <= right:
        mid = (left + right) // 2
        
        result = 0
        print(left, right, mid, result)
        if left == right:
            return 0
        for i in range(N-1, -1, -1):
            if data[i] < mid :
                break
            result += data[i] - mid
        print(result)
        if result < M:
            right = mid
        elif result > M:
            left = mid + 1
        else:
            return mid
N, M = map(int, input().split())
data = list(map(int, (input().split())))
data.sort()
print(solve())