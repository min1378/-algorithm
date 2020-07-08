def solution(strings, n):
    temps = []
    for string in strings:
        temps.append(string[n] + string)
    temps.sort()
    answer = []
    for temp in temps:
        answer.append(temp[1:])
    return answer




# 다른방법
def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda strings: strings[n]) 

print(solution(["sun", "bed", "car"], 1))