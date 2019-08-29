import sys
sys.stdin = open('shuffle.txt', 'r')
TC = int(input())

def check(result):
    flag = True

    for i in range(len(result)-1):
        if result[i] + 1 != result[i+1]:
            flag = False
            break

    if flag == True:
        return True

    for i in range(len(result)-1, 0, -1):
        if result[i] - 1 != result[i-1]:
            flag = False
            break
        flag = True

    if flag == True:
        return True

    if flag == False:
        return False
for test_case in range(1, TC+1):
    N = int(input())
    temp = list(map(int, input().split()))



    for i in range(6):
        temp1 = temp[0:N // 2]
        temp2 = temp[N // 2:N]
        result = 0
        if i > N-1:
            x = -1
            break
        for j in range(i):
            temp1.insert((len(temp1)-1)-(j-1),temp2[j-1])

        temp1.extend(temp2[i:len(temp2)])
        result = temp1
        print(result)
        answer = check(result)

        if answer == True:
            x = i
            break

    print("#{} {}".format(test_case, x))
