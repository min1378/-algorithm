def solution(ip_addrs, langs, scores):
    answer = 0
    ipdic = {}
    for i in range(len(ip_addrs)):
        ip = ip_addrs[i]
        lang = langs[i]
        score = scores[i]
        if ip in ipdic.keys():
            ipdic[ip].append([lang, score])
        else:
            ipdic[ip] =[[lang, score]]
    
    for value in ipdic.values():
        if len(value) == 3:
            count = [0, 0, 0, 0] # c, java, js, python
            for el in value:
                if el[0] == "C":
                    count[0] += 1
                elif el[0] == "P":
                    count[3] += 1
                elif el == "Java":
                    count[1] += 1
                else:
                    count[2] += 1
            if 3 in count:
                continue
            else:
                answer += 3
        if len(value) == 2:
            if value[0] == value[1]:
                continue
            else:
                answer += 2
    return answer


print(solution(["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373]))
print(solution(["7.124.10.0", "7.124.10.0", "0.0.0.0", "7.124.10.0", "0.0.0.0", "7.124.10.0"], ["C++", "Java", "C#", "C#", "C", "Python3"], [314, 225, 45, 0, 155, 400]))