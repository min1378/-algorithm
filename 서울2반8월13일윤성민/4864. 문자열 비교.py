import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())
    check= 0
    for i in range(len(str2)-len(str1)+1):
        temp = ''
        for j in range(len(str1)):
            temp += str2[i+j]
        if temp == str1:
            check = 1

    print('#{} {}'.format(test_case, check))