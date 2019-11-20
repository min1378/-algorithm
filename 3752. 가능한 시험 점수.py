import sys
sys.stdin = open('3752.txt', 'r')
TC = int(input())
def comb(number, count):
    global answer
    if number == N:
        if count not in answer:
            answer.append(count)
        return
    if count in answer:
        return
    comb(number+1, count + data[number])
    comb(number+1, count)



for test_case in range(1, TC+1):
    N = int(input())
    data = list(map(int, input().split()))
    print(data)
    answer = []
    dp = [True] + [False] * sum(data)
    temp = [0]
    for i in data:
        for j in range(len(temp)):
            if dp[temp[j]+i] == False:
                print(temp[j], i)
                dp[temp[j]+i] = True
                temp.append(temp[j]+i)

    print("#{} {}".format(test_case,len(temp)))