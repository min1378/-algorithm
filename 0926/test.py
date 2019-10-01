import sys
from pprint import pprint
sys.stdin = open('test.txt', 'r')

Base_line = float(input())
dic = {}
N = 3126//2
for _ in range(N):

    temp = str(input())
    temp3 = temp.split(':',1)[1].split('/',1)[0].strip()

    if temp3.split('_',2)[0].strip() =='P' or temp3.split('_',2)[0].strip() =='R':
        feature = temp3.split('_', 2)[0].strip() + '_' + temp3.split('_', 2)[1].strip() + '__' + temp3.split('_', 2)[2].strip()
    else:
        feature = temp3.split('_', 1)[0].strip() + '__' + temp3.split('_', 1)[1].strip()
    temp2 = str(input())
    score = float(temp2.split('=',1)[1].strip())
    dic[feature] = score

pprint(dic)
