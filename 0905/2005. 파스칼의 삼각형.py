import sys
import itertools
sys.stdin = open('2005.txt', 'r')
TC =int(input())
for test_case in range(1, TC+1):
    N = int(input())
    if N == 1:
        result = [[1]]
    elif N == 2:
        result = [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, N):
            temp = [1] * (i+1)
            for j in range(i-1):
                temp[j+1] = result[i-1][j] + result[i-1][j+1]
            result.append(temp)
    print("#{}".format(test_case))
    for line in result:
        final = ''
        for i in range(len(line)):
            final += str(line[i]) + ' '
        print(final)

