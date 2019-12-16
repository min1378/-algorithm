TC = int(input())

for test_case in range(1, TC+1):
    N1, N2 = list(map(int, input().split()))

    basis_1 = 0
    count_1 = 1
    while basis_1 < N1:
        basis_1 += count_1

        if basis_1 >= N1:
            break
        count_1 += 1

    diff = basis_1 - N1
    N1_x = count_1 - diff
    N1_y = 1 + diff
    # print(N1_x, N1_y)


    basis_2 = 0
    count_2 = 1
    while basis_2 < N2:
        basis_2 += count_2

        if basis_2 >= N2:
            break
        count_2 += 1

    diff = basis_2 - N2
    N2_x = count_2 - diff
    N2_y = 1 + diff
    # print(N2_x, N2_y)


    x = N1_x + N2_x
    y = N1_y + N2_y


    basis = 0
    count = 0
    for _ in range(x+y):
        basis += count
        count += 1
        # print(count-1)
        # print(basis)

    ans = basis - (count - 1 - x)
    print('#%s %s' % (test_case, ans))