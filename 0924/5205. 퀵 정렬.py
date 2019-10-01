import sys
sys.stdin = open('5205.txt', 'r')
TC = int(input())
def quick(data, start, end):
    if start >= end :
        return
    pivot = data[start]
    left = start
    right = end
    while left < right:
        while (data[left] <= pivot) and (left < end):
            left += 1
        while (data[right] > pivot) and (right >= start):
            right -= 1



        if left < right:
            data[left], data[right] = data[right], data[left]

    data[start], data[right] = data[right], data[start]
    print(data, pivot, left, right)
    quick(data, start, right-1)
    quick(data, right+1, end)

for test_case in range(1, TC+1):
    N = int(input())
    data = list(map(int, input().split()))

    quick(data, 0, N-1)

    print("#{} {}".format(test_case, data[N//2]))