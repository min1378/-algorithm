def comb(k, now, temp):
    #print(now, temp)
    global result
    if k == 4:
        result.append(temp)
    else:
        for i in range(now+1, N + 1):
            comb(k+1, i, temp + [i])
N = 6
result = []
comb(0, 0, [])
print(result)

