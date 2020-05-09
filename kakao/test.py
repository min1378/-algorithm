def test(char):
    check = char.split("#")
    for i in range(len(check) - 1):
        temp = check[i][-1].lower()
        check[i] = check[i][:len(check[i]) - 1] + temp

    new_check = "".join(check)


print(test("AA#ABC#"))