import sys

sys.stdin = open('4869.txt', 'r')

def paper(w):
    if w == n : #목표너비가 되면
        return 1
    if w > n : #목표너비보다 크면
        return 0
    return paper(w+10) + paper(w+20) * 2
TC = int(input())
for tc in range(1, TC+1):
    n = int(input()) #너비
    r = paper(0)
    print('#%d %d' % (tc, r))