


print(__name__)

def mysum(num):
    n = 3 + 2 + 1

def mysum(num):
    #멈춤조건
    if num == 1 :
        return 1
    #재귀
    return num + mysum(num-1)
n = mysum(3)
print(n)




