lst = [10, 5, 8, 3]


def modify_list(numbers):
    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            numbers[i] //= 2
        else:
            numbers.pop(i)
            i -= 1
        i += 1


modify_list(lst)
print(lst)
