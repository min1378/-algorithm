def returns(num1, x):
    ls = []
    ans = 0
    ls.append(num1)
    ls.append(x)
    count = 0
    while True :
        ans = ls[count] - ls[count+1]
        if ans >= 0 :
            ls.append(ans)
        if ls[count+1] >= ans :
            count += 1            
        else :
            return ls

num1 = int(input())
result = []

for i in range(num1//2, num1+1, 1):
    temp = returns(num1,i)
    if len(result) < len(temp):
        result = temp
print(result, len(result))    