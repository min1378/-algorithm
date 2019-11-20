def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0


    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        count +=1
        if guess == item:
            return mid, count

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1


    return None, count


my_list = [i for i in range(1, 101)]
print(my_list)
print(binary_search(my_list, 5)) # => (4, 7)
print(binary_search(my_list, 101)) # => (None, 7)