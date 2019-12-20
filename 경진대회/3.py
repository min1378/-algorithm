import sys
sys.stdin = open('3.txt', 'r')

def solve():
    index = -1
    global temp_result
    global result
    for i in range(digit):
        Ni = int(str_N[i])
        for number in numbers:
            if Ni >= number:
                temp_result[i] = number
                if number == y:
                    index = i
                    break
                if Ni > number:
                    index = i
                    for ii in range(index + 1, digit):
                        temp_result[ii] = y
                    return
        if temp_result[i] == 0:
            if index == -1:
                result = False
                return
            else:
                temp_result[index] = x
                for ii in range(index + 1, digit):
                    temp_result[ii] = y
                return

TC = int(input())
for test_case in range(1, TC+1):
    N, x, y = map(int, input().split())
    str_N = str(N)
    digit = len(str_N)
    numbers = (y, x)
    temp_result = [0] * digit
    result = True
    solve()
    if sum(temp_result) == 0:
        result = False
    if not result:
        print("#{} {}".format(test_case, -1))
    else:
        temp = ''
        print("#{} {}".format(test_case, int(temp.join(map(str, temp_result)))))
