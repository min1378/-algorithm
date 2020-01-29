import sys
sys.stdin = open('input2455.txt', 'r')
max_count = 0
result = 0
for _ in range(4):
    down, up = map(int, input().split())
    result += up
    result -= down
    max_count = max(result, max_count)

print(max_count)