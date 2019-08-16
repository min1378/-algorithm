import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    str1 = str(input())
    str2 = str(input())
    result = 0
    for i in range(len(str1)):
        count = 0
        if i >= 1:
            check = False
            for k in range(i):
                if str1[i] == str1[k]:
                    check = True
                    break            
            if check == True:
                continue
        for j in range(len(str2)):            
            if str1[i] == str2[j]:
                count += 1
        if count > result :
            result = count
    print('#{} {}'.format(test_case, result))
