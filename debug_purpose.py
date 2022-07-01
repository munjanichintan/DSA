def bubble_sort(x):

    for i in range(len(x) - 1):
        swapped = False
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
                swapped = True

        if swapped == False:
            break
    return x


x = [2, 1, 3, 4, 5]
bubble_sort(x)
print(x)
