def solution(S, C):  # 이름 중간이름 성
    # write your code in Python 3.6 # 이름.성@회사이름.com
    company = S.lower()
    names = C.split(";")
    email_dict = {}
    result = []
    for name in names:
        split_name = name.strip().split(" ")
        first_name = split_name[0].strip().lower()
        last_name = "".join(
            split_name[-1].strip().split("-")).strip().lower()[:8]
        email = f'{first_name}.{last_name}@{company}.com'
        if (email in email_dict):
            email_dict[email] += 1
            number = email_dict.get(email)
            email = f'{first_name}.{last_name}{number}@{company}.com'
        else:
            email_dict[email] = 1
        result.append(f'{name} <{email}>')
    print(";".join(result) + '.')
    return ";".join(result) + '.'.strip()


solution(
    "Example",
    "John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
)
