def solution(s):
    answer = 0
    s = list(map(str, s))

    while True:
        check = []

        N = len(s)
        if N == 0:
            answer = 1
            return answer

        i = 0

        while True:
            if i >= N-1:
                break
            if s[i] == s[i + 1]:
                check.append(i)
                i += 2
            else:
                i += 1

        if check == [] and s != []:
            answer = 0
            return answer
        for i in range(len(check)-1, -1, -1):

            s.pop(check[i])
            s.pop(check[i])
            for i in range()
result =solution('cabbac')
print(result)