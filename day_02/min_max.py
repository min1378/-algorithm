

T = int(input())
for test_case in range(1, T + 1):

    size = int(input())
    numbers = [0]*size
    numbers = list(map(int, input().split()))
    n_max = numbers[0]
    n_min = numbers[0]

    for i in range(size) :
        if n_max < numbers[i]:
            n_max = numbers[i]
        if n_min > numbers[i]:
            n_min = numbers[i]
    result = n_max - n_min
    print('#{} {}'.format(test_case, result))