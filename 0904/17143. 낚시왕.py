import sys
from pprint import pprint
sys.stdin = open('17143.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    R, C, M = map(int,(input().split()))
    shark_data = [list(map(int, input().split())) for _ in range(M)]

    print(R, C, M)
    pprint(shark_data)
    count = 0

    while True:
        count += 1
        if count == R:
            break

        