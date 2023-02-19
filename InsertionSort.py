def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print("\n")

arr = [80, 90, 60, 30, 50, 70, 40]
insertion_sort(arr)
print_array(arr)
