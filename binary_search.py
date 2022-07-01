def binary_search(arr1, find_value1):
    left_index = 0
    right_index = len(arr1) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = arr1[mid_index]

        if find_value == mid_value:
            return mid_index
        elif find_value < mid_index:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1

    return -1


def find_all_occurances(arr1, find_value1):
    index = binary_search(arr1, find_value1)

    indices = [index]

    i = index - 1
    while i >= 0:
        if find_value1 == arr1[i]:
            indices.append(i)
        else:
            break
        i -= 1

    i = index + 1
    while i <= len(arr1):
        if find_value1 == arr1[i]:
            indices.append(i)
        else:
            break
        i += 1

    return sorted(indices)


def binary_search_recursion(arr1, find_value1, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_value = arr1[mid_index]

    if find_value1 == mid_value:
        return mid_index

    elif find_value < mid_value:
        right_index = mid_index - 1

    else:
        left_index = mid_index + 1

    return binary_search_recursion(arr1, find_value1, left_index, right_index)


arr = [12, 23, 44, 55, 55, 55, 67, 80, 89]
find_value = 55
print(binary_search_recursion(arr, find_value, 0, len(arr) - 1))
print(find_all_occurances(arr, find_value))
