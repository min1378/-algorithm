binary = []
tri = []
from pprint import pprint
for i in range(1, 51):
    answer = i
    result = ''
    while True:
        re = answer % 2
        result = str(re) + result
        answer = answer // 2
        if answer < 2:
            result = str(answer) + result
            break
    binary.append(result)
    answer = i
    result2 = ''
    while True:
        re = answer % 3
        result2 = str(re) + result2
        answer = answer // 3
        if answer < 3:
            result2 = str(answer) + result2
            break
    tri.append(result2)


for i in range(1, 51):
    print(i, binary[i], tri[i])