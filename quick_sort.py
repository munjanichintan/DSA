def swap(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, arr)
    swap(pivot_index, end, arr)

    return end

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

if __name__ == "__main__":
    arr = [7,5,8,45,12,54,52,5,5,56]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)