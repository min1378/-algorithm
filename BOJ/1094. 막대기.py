import sys
sys.stdin = open('i1094.txt', 'r')
from collections import deque
TC = 4

for test_case in range(1, TC+1):
    X = int(input())
    print(list(bin(X)).count('1'))
    


    
