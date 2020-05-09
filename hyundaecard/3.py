
def check(string):
    for s in string:
        if ord("a") <= ord(s) <= ord("z"):
            continue
        return string[:string.index(s)],int(string[string.index(s):])
    return string, 0
def solution(registered_list, new_id):
    answer = ''
    temp_id = new_id
    string, number = check(temp_id)
    while True:
        if temp_id not in registered_list:
            answer = temp_id
            return answer
        number += 1
        temp_id = string + str(number)

print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(["apple1", "orange", "banana3"], "apple"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))