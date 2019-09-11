first = [273, 415, 58, 798, 251]

second = [675, 193, 494, 506, 365]

for i in range(len(first)):
    if first[i] > second[0]:
        check = i
        break
print(check)
print(first[check:check+len(second)-1])

first[check:check+len(second)] = second + first[check:check+len(second)]

print(first)

