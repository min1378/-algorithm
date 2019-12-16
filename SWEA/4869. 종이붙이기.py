import sys
sys.stdin = open("input.txt", "r")
              
def calcul(x) :
    if x == 0:
        return 1
    if x < 0:
        return 0
    
    return calcul(x-10) + calcul(x-20) * 2

T = int(input())
for test_case in range(1, T + 1):
    x = int(input())
    result = calcul(x)       
    print('#{} {}'.format(test_case, result))