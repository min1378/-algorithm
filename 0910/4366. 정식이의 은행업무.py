import sys
sys.stdin = open('4366.txt', 'r')
def intersect(a, b):
    return list(set(a) & set(b))

TC = int(input())
for test_case in range(1, TC+1):
    wrong_binary = str(input())
    wrong_tri = str(input())
    base_1 = 2
    base_2 = 3
    first = int(wrong_binary, base_1)
    second = int(wrong_tri, base_2)

    check_binary = []
    check_tri = []

    temp = wrong_binary
    for i in range(len(temp)):
        if i == len(temp) - 1:
            continue
        if temp[len(temp)-i-1] == '0':
            check_binary.append(first + 2**i)
        elif temp[len(temp)-i-1] == '1':
            check_binary.append(first - 2**i)



    temp2 = wrong_tri

    i = 0
    count = 0
    while len(temp2) != i:
        if i == len(temp2) -1 :
            if temp2[len(temp2) - i - 1] == '1':
                count = 1
                check_tri.append(second + count * 3 ** i)
            elif temp2[len(temp2) - i - 1] == '2':
                count = 1
                check_tri.append(second - count * 3 ** i)
            break
        if temp2[len(temp2)-i-1] == '0':
            count += 1
            check_tri.append(second + count * 3 **i)
            count += 1
            check_tri.append(second + count * 3 ** i)
        elif temp2[len(temp2)-i-1] == '1':
            count += 1
            check_tri.append(second - count * 3 **i)
            check_tri.append(second + count * 3 ** i)
        elif temp2[len(temp2)-i-1] == '2':
            count += 1
            check_tri.append(second - count * 3 ** i)
            count += 1
            check_tri.append(second - count * 3 ** i)

        count = 0
        i += 1
    
    if first > second :
        left = second
        right = first
    else:
        left = first
        right =second
    temp3 = intersect(check_binary, check_tri)

    print("#{} {}".format(test_case, temp3[0]))









