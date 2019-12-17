import sys
sys.stdin = open('1920.txt', 'r')


def binary_check(left, right, number):
    while right - left >= 0:
        mid = (left + right) // 2

        if number > data[mid] :
            left = mid + 1
        elif number < data[mid]:
            right = mid - 1
        elif number == data[mid]:
            print("1")
            return

    print("0")
    return



N = int(input())
data = list(map(int, input().split()))
data.sort()
M = int(input())
numbers = list(map(int, input().split()))
for i in range(M):
    binary_check(0, N-1, numbers[i])
