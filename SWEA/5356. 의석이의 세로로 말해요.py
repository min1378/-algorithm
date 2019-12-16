import sys
sys.stdin = open('5356.txt', 'r')
TC = int(input())
for test_case in range(1, TC+1):
    data = []
    for _ in range(5):
        temp = list(map(str, input()))
        data.append(temp)
    result = ''
    max = 0
    for line in data:

        if max < len(line):
            max = len(line)
    for i in range(max):
        for j in range(5):

            if i > len(data[j]) - 1:

                continue
            else:

                result += data[j][i]
    print("#{} {}".format(test_case, result))
    # Aa0FfBb1GgCc2HhDd3IiEe4Jj
    # Aa0FfBb1GgCc2HhDd3IiEe4Jj
    #
    # Aa0aPAf985Bz1EhCz2W3D1gkD6x
    # Aa0aPAf985Bz1EhCz2W3D1gkD6x