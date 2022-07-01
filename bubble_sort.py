# define function for bubble sort.
def bubble_sort(x):
    l = len(x)
    for i in range(l-1):
        swapped = False
        for j in range(l-1-i):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
                swapped = True

        if swapped == False:
            break



# list as a input
# x = [1, 41, 34, 30, 42, 55, 33]
x = [1, 2, 3, 4]
bubble_sort(x)
print(x)