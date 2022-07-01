def insertion_sort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1

        x[j+1] = key

x = [10, 20, 30, 4, 3, 21, 1]
insertion_sort(x)
print(x)