def solution(ip_addrs, langs, scores):
    def check_lang(lang):
        if lang == "C" or lang == "C++" or lang == "C#":
            return "C_friends"
        else:
            return lang

    answer = 0
    length = len(ip_addrs)
    ip_dict = {}
    for i in range(length):
        if ip_dict.get(ip_addrs[i]): # 있다면!!!
            ip_dict[ip_addrs[i]].append([langs[i], scores[i]])
        else:
            ip_dict[ip_addrs[i]] = [ [langs[i], scores[i]] ]
    # print(ip_dict)
    for value in ip_dict.values():
        # print(value)
        if len(value) >= 4:
            continue
        elif len(value) == 3:
            a = check_lang(value[0][0])
            b = check_lang(value[1][0])
            c = check_lang(value[2][0])
            if a == b == c:
                continue
            else:
                answer += 3
        elif len(value) == 2:
            a = check_lang(value[0][0])
            b = check_lang(value[1][0])
            if a == b and value[0][1] == value[1][1]:
                continue
            else:
                answer += 2
        else:
            answer += 1
    return answer

solution(["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373])