def selection_sort(x):
    for i in range(len(x)-1):
        min_index = i
        for j in range(min_index+1, len(x)):
            if x[j] < x[min_index]:
                min_index = j
        if i != min_index:
            x[i], x[min_index] = x[min_index], x[i]

x = [10, 20, 30, 4, 3, 2, 1]
selection_sort(x)
print(x)