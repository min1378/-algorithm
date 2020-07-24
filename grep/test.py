bit = [0] * 100001 
a = [0] * 100000
dp = [0] * 100000
def maxInversion(arr):
    for i in range(len(arr)):
        a[i] = arr[i]
        dp[i] = 1
        
    for i in range(2, 3):
        for j in range(len(arr)):
            h = a[j]
            while h <= 100000:
                bit[h] = (bit[h] + dp[j])
                h += h&(-h)
                dp[j] = 0
            while h <= h
            for h in range(a[j]-1, 100000):
                dp[j] = (dp[j] + bit[h])
        
    
    s = 0
    for i in range(len(arr)):
        s = (s + dp[i])
    print(s)
    return
maxInversion([5, 2, 4, 3, 1])