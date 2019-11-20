import sys
sys.stdin = open('5207.txt', 'r')
TC = int(input())

def compare(left, right, check, temp):

    global count
    mid = (left + right) // 2

    if check == data[mid]:
        count += 1
        return

    elif left >= right:
        return

    elif temp == 2:
        temp = 1
        left = mid + 1
        compare(left, right, check, temp)

    elif temp == 1:
        temp = 2
        right = mid - 1
        compare(left, right, check, temp)



def binary(data, start, end):
    global count
    for check in search:
        left = start
        right = end
        mid = (left + right) // 2
        if check > data[mid]:
            temp = 1
            left = mid + 1
            compare(left, right, check, temp)

        elif check < data[mid]:
            temp = 2
            right = mid - 1
            compare(left, right, check, temp)

        else:
            count += 1


for test_case in range(1, TC+1):
    N,M = map(int, (input().split()))
    data = list(map(int, input().split()))
    data.sort()

    search = list(map(int, input().split()))
    search.sort()
    count = 0
    binary(data, 0, len(data)-1)
    print("#{} {}".format(test_case, count))