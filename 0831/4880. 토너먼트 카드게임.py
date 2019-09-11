import sys
sys.stdin = open('4880.txt', 'r')

def divi(line):
    global divi_count
    if line == 1 or line == 2:
        divi_count.append(line)
        return 0
    line2 = line - line//2
    return divi(line2) + divi(line - line2)

def merge(list):
    global divi_count

def fight(one, two):

    if (one == 1 and two == 3) or (one == 2 and  two == 1) or (one == 3 and two == 2):
        return 100
    elif (one == 1 and two == 2) or (one == 2 and two == 3) or (one == 3 and two == 1) :
        return 200
    elif one == two :
        return 99


TC= int(input())
for test_case in range(1, TC+1):
    N = int(input())
    divi_count = []
    data = list(map(int, input().split()))
    divi(N)
    order = 0
    temp = []
    for i in range(len(data)):
        temp.append([data[i],i])

    for i in range()





