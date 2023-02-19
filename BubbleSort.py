def bubbleSort(arr):
    c = 0
    flag = True

    for i  in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] >  arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
            
            c += 1

        if flag:
            break
    print("# of rounds:", c)
def printArray(arr):
    print(*arr)

arr = [30, 20, 40, 5, 60, 2]
bubbleSort(arr)
printArray(arr)
