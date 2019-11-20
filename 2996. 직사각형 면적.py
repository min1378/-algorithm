import sys
sys.stdin = open("sample_input.txt", "r")
def check(ls, sketch):
    width = ls[2]-ls[0]
    height = ls[3]-ls[1]
    for i in range(width):
        for j in range(height):
            sketch[ls[0]+i][ls[1]+j] = 1       


T=1
for test_case in range(1, T + 1):
    result = 0
    sketch = []
    for i in range(100) :
        temp=[]
        for j in range(100):
            temp.append(0)
        sketch.append(temp)
    size1 = list(map(int, input().split()))
    size2 = list(map(int, input().split()))
    size3 = list(map(int, input().split()))
    size4 = list(map(int, input().split()))
    check(size1, sketch)
    check(size2, sketch)
    check(size3, sketch)
    check(size4, sketch)
    for i in range(100) :
        for j in range(100):
            if sketch[i][j] == 1:
                result +=1
    print(result)