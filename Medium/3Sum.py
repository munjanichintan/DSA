def f(arr):
    arr.sort()
    print(arr)
    x = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        (j, k) = (i+1, len(arr)-1)
        while j < k:
            sum = arr[i] + arr[j] + arr[k]

            if sum == 0:
                x.append([arr[i], arr[j], arr[k]])
                k -= 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
            elif sum < 0:
                j += 1
            else:
                k -= 1
    return x


if __name__ == "__main__":
    arr = [-4, -1, -1, 0, 1, 2]
    print(f(arr))
