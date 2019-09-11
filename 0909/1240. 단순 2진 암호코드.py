import sys
from pprint import pprint
sys.stdin = open('1240.txt', 'r')
def pattern_check(str1):
    if str1[0] == '0' and str1[1] == '0' and str1[2] == '0' :
        if str1[4] == '1' :
            return 0
        else :
            return 9

    elif str1[0] == '0' and str1[1] == '0':
        if str1[3] == '1':
            return 1
        else :
            return 2

    elif str1[0] == '0':
        if str1[2] == '0':
            if str1[3] == '0':
                return 4
            else :
                return 6
        else:
            if str1[3] == '0':
                if str1[4] == '0':
                    return 5
                else:
                    return 8
            else:
                if str1[4] == '0':
                    return 7
                else :
                    return 3



TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split())
    password = []
    for i in range(N):
        temp = str(input())
        if '1' in temp:
            password.append(temp)
    flag = True
    check = password[0]
    for i in check:
        if i != '0' and i != '1':
            flag = False
    for line in password:
        if line != check:
            flag = False

    if flag == False:
        print("#{} {}".format(test_case, 0))


    else:
        for i in range(len(check)):
            if check[i] == '1':
                first = i
                break
        for i in range(len(check)-1, -1, -1):
            if check[i] == '1':
                last = i
                break

        first -= 56 - (last-first+1)

        if first < 0:
            print("#{} {}".format(test_case, 0))

        else :
            check_list = []

            for k in range(8):
                temp = ''
                for i in range(first + 7*k, first + 7*k + 7):

                    temp += check[i]
                check_list.append(temp)


            last = []
            for str1 in check_list:
                temp = pattern_check(str1)

                last.append(temp)

            result =(last[0] + last[2] + last[4] + last[6])*3 + last[1] +last[3] + last[5] + last[-1]
            if result % 10 != 0:
                result = 0

            else:
                result = sum(last)
            print("#{} {}".format(test_case, result))

