test = [1, 2, 3]

if 1 in test:
    idx = test.index(1)
    test.pop(idx)
    print(idx, test)