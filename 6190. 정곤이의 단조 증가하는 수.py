import sys
import itertools
import copy
sys.stdin = open('6190.txt', 'r')
TC= int(input())
for test_case in range(1, TC+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print(data)
    data.reverse()




    max = -1
    check = False

    for i in range(len(data)):
        for j in range(len(data)):

            if i <= j:
                continue

            s=str(data[i] * data[j])
            print(s)
            for k in range(len(s)-1):

                if s[k] > s[k+1]:
                    check = False
                    break
                if k == len(s)-2 and s[k] <= s[k+1]:
                    if int(s) > max:
                        max=int(s)




    print("#{} {}".format(test_case, max))




