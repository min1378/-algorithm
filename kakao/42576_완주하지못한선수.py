def solution(participant, completion):
    answer = ''
    last_hash = 0
    dic = {}
    for part_person in participant:
        print(part_person, hash(part_person))
        dic[hash(part_person)] = part_person
        last_hash += int(hash(part_person))
        print(last_hash)
    print(dic)
    
    for comple_person in completion:
        last_hash -= hash(comple_person)
        print(last_hash)
    answer = dic[last_hash]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
